import descriptive_statistics

import pandas as pd

import data_preparer

file_name = "wdbc.csv"

data = pd.read_csv(file_name)
class_column = data_preparer.get_class_column(data)
data = data_preparer.get_data_with_filled_gaps(data)
data = data_preparer.get_data_for_statistics(data)
data.to_csv("prepared_" + file_name, index=False)
print('Prepared data.')

descriptive_statistics.generate_ranges_report(data, "ranges.csv")
descriptive_statistics.generate_averages_report(data, "averages.csv")
descriptive_statistics.generate_standard_report(data, "standard_deviations.csv")
descriptive_statistics.generate_medians_report(data, "medians.csv")
descriptive_statistics.generate_iqr_ranges_report(data, "iqr_ranges.csv")
descriptive_statistics.generate_quantiles_report(data, "quantiles_01.csv", 0.1)
descriptive_statistics.generate_quantiles_report(data, "quantiles_09.csv", 0.9)
print('Generated statistics report.')
