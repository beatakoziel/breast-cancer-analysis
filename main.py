import descriptive_statistics

import pandas as pd

import data_preparer

file_name = "wdbc.csv"

raw_data = pd.read_csv(file_name)
class_column = data_preparer.get_class_column(raw_data)
statistics_data = data_preparer.get_data_for_statistics(raw_data)
statistics_data.to_csv("statistics_data.csv", index=False)
print('Prepared data.')

descriptive_statistics.generate_ranges_report(statistics_data, "ranges.csv")
descriptive_statistics.generate_averages_report(statistics_data, "averages.csv")
descriptive_statistics.generate_standard_report(statistics_data, "standard_deviations.csv")
descriptive_statistics.generate_medians_report(statistics_data, "medians.csv")
descriptive_statistics.generate_iqr_ranges_report(statistics_data, "iqr_ranges.csv")
descriptive_statistics.generate_quantiles_report(statistics_data, "quantiles_01.csv", 0.1)
descriptive_statistics.generate_quantiles_report(statistics_data, "quantiles_09.csv", 0.9)
print('Generated statistics reports.')

descriptive_statistics.get_outliers_report(statistics_data, "outliers.csv")
descriptive_statistics.get_outliers_counters_report(statistics_data, "outliers_counters.csv")
descriptive_statistics.get_pearson_attributes_correlation_report(statistics_data, "pearson_attributes_correlation.csv")
descriptive_statistics.get_pearson_class_correlation_report(statistics_data, "pearson_class_correlation.csv", class_column)
