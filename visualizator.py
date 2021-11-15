from matplotlib import pyplot
from sklearn.linear_model import LinearRegression


def create_histograms(data):
    data.hist(density=True)
    pyplot.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.6)
    pyplot.show()


def create_linear_regression_diagram(data, column_name_1, column_name_2):
    x = data[column_name_1].values.reshape(-1, 1)
    y = data[column_name_2].values.reshape(-1, 1)

    linear_regressor = LinearRegression()
    linear_regressor.fit(x, y)
    predictions = linear_regressor.predict(x)

    pyplot.scatter(x, y)
    pyplot.xlabel(column_name_1)
    pyplot.ylabel(column_name_2)
    pyplot.plot(x, predictions, color='black')
    pyplot.show()


def create_attributes_values_diagram(data):
    data.plot(subplots=True, layout=(4, 4))
    pyplot.show()


def create_box_diagrams(data):
    data.boxplot()
    pyplot.xticks(rotation=20)
    pyplot.show()
