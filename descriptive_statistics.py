import csv
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot
import numpy


def generate_ranges_report(data, file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["column_name", "min", "max"])
        for col in data.columns:
            writer.writerow([col, data[col].min(), data[col].max()])


def generate_averages_report(data, file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["column_name", "average"])
        for col in data.columns:
            writer.writerow([col, data[col].mean().round(3)])


def generate_standard_report(data, file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["column_name", "standard_deviation"])
        for col in data.columns:
            writer.writerow([col, data[col].std().round(3)])


def generate_medians_report(data, file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["column_name", "median"])
        for col in data.columns:
            writer.writerow([col, data[col].median().round(3)])


def generate_iqr_ranges_report(data, file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["column_name", "iqr_range"])
        for col in data.columns:
            writer.writerow([col, calculate_iqr_ranges(data, col).round(3)])


def generate_quantiles_report(data, file_name, range):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["column_name", "quantile_range_" + str(range)])
        for col in data.columns:
            writer.writerow([col, numpy.quantile(data[col], range).round(3)])


def calculate_iqr_ranges(data, col):
    q3 = numpy.quantile(data[col], 0.75)
    q1 = numpy.quantile(data[col], 0.25)
    return q3 - q1


def get_outliers_report(data, file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["column_name", "attribute"])
        for col in data.columns:
            q3 = numpy.quantile(data[col], 0.75)
            q1 = numpy.quantile(data[col], 0.25)
            iqr = q3 - q1
            lower_range = q1 - (1.5 * iqr)
            upper_range = q3 + (1.5 * iqr)
            for val in data[col]:
                if val < lower_range or val > upper_range:
                    writer.writerow([col, val])


def get_outliers_counters_report(data, file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["column_name", "outliers_count"])
        for col in data.columns:
            q3 = numpy.quantile(data[col], 0.75)
            q1 = numpy.quantile(data[col], 0.25)
            iqr = q3 - q1
            lower_range = q1 - (1.5 * iqr)
            upper_range = q3 + (1.5 * iqr)
            counter = 0
            for val in data[col]:
                if val < lower_range or val > upper_range:
                    counter = counter + 1
            writer.writerow([col, counter])


def get_pearson_attributes_correlation_report(data, file_name):
    data.corr(method="pearson").to_csv(file_name)


def get_pearson_class_correlation_report(data, file_name, class_column):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["column_name", "pearson_correlation"])
        for col in data.columns:
            writer.writerow([col, numpy.corrcoef(class_column.astype(float), data[col].astype(float))[0][1]])


def get_linear_regression_report(data, column_name_1, column_name_2, file_name):
    x = data[column_name_1].values.reshape(-1, 1)
    y = data[column_name_2].values.reshape(-1, 1)

    linear_regressor = LinearRegression()
    linear_regressor.fit(x, y)
    predictions = linear_regressor.predict(x).flatten()
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([column_name_1, column_name_2, "predicted"])
        for index, row in data.iterrows():
            writer.writerow([data[column_name_1][index], data[column_name_2][index], predictions[index]])
