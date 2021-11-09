import csv

import numpy


def generate_ranges_report(data, file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["column_name", "min", "max"])
        for col in data.columns:
            writer.writerow([col, data[col].min(), data[col].max()])


def generate_averages_report(data, file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["column_name", "average"])
        for col in data.columns:
            writer.writerow([col, data[col].mean().round(3)])


def generate_standard_report(data, file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["column_name", "standard_deviation"])
        for col in data.columns:
            writer.writerow([col, data[col].std().round(3)])


def generate_medians_report(data, file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["column_name", "median"])
        for col in data.columns:
            writer.writerow([col, data[col].median().round(3)])


def generate_iqr_ranges_report(data, file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["column_name", "iqr_range"])
        for col in data.columns:
            writer.writerow([col, calculate_iqr_ranges(data, col).round(3)])


def generate_quantiles_report(data, file_name, range):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["column_name", "quantile_range_" + str(range)])
        for col in data.columns:
            writer.writerow([col, numpy.quantile(data[col], range).round(3)])


def calculate_iqr_ranges(data, col):
    q3 = numpy.quantile(data[col], 0.75)
    q1 = numpy.quantile(data[col], 0.25)
    return q3 - q1
