from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def classify(data):
    y = data['diagnosis']
    x = data.drop(labels=['diagnosis'], axis=1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)  # 70% training and 30% test
    clasifier = RandomForestClassifier(n_estimators=100)

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




def generate_feature_importance_report(feature_imp):
    sns.barplot(x=feature_imp, y=feature_imp.index)
    plt.xlabel('feature importance score')
    plt.ylabel('features')
    plt.title("Important features report")
    plt.legend()
    plt.show()
