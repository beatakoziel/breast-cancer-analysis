import pydot as pydot
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_validate
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import export_graphviz
import os
from subprocess import check_call


def classify(data):
    y = data['diagnosis']
    x = data.drop(labels=['diagnosis'], axis=1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)  # 70% training and 30% test

    clasifier = RandomForestClassifier(n_estimators=2, max_depth=100, max_samples=100)  # dla roznej liczby jak wplynie na wyniki i rozne parametry
    # w tabelce wpisujemy ze ustawilismy takie dane i uzyskalismy takie accuracy, opisać drzewa losowe, parametry które zostały użyte
    # train the model using the training sets
    clasifier.fit(x_train, y_train)
    y_pred = clasifier.predict(x_test)

    # how often is the classifier correct?
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
    print("Average precision score: ",
          metrics.average_precision_score(y_test, y_pred))

    # finding important features
    feature_imp = pd.Series(clasifier.feature_importances_, index=list(x.columns)).sort_values(ascending=False)
    print(feature_imp)
    generate_feature_importance_report(feature_imp)

    for i in range(0, len(clasifier.estimators_)):
        export_graphviz(clasifier.estimators_[i], out_file=f"tree-{i}.dot", feature_names=x.columns,
                        class_names="diagnosis", rounded=True, proportion=False, precision=2, filled=True)
        check_call(['dot', '-Tpng', f"tree-{i}.dot", '-o', f"tree-{i}.png"])

    # 5 rauruchomic i inne dane


def generate_feature_importance_report(feature_imp):
    sns.barplot(x=feature_imp, y=feature_imp.index)
    plt.xlabel('feature importance score')
    plt.ylabel('features')
    plt.title("Important features report")
    plt.legend()
    plt.show()


def classify_kfold(data, folds):
    y = data['diagnosis']
    x = data.drop(labels=['diagnosis'], axis=1)

    model = RandomForestClassifier(random_state=1)
    cv = cross_validate(model, x, y, cv=folds)

    print(cv["test_score"].mean())
