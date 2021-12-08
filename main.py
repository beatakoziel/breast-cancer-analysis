import matplotlib
import descriptive_statistics
import pandas as pd
import data_preparer
import visualizator
import random_forest

file_name = "wdbc.csv"
matplotlib.rcParams.update({'font.size': 6})
raw_data = pd.read_csv(file_name)
class_column = data_preparer.get_class_column(raw_data)
# statistics_data = data_preparer.get_data_for_statistics(raw_data)
# print('Prepared data.')

# descriptive_statistics.generate_ranges_report(statistics_data, "ranges.csv")
# descriptive_statistics.generate_averages_report(statistics_data, "averages.csv")
# descriptive_statistics.generate_standard_report(statistics_data, "standard_deviations.csv")
# descriptive_statistics.generate_medians_report(statistics_data, "medians.csv")
# descriptive_statistics.generate_iqr_ranges_report(statistics_data, "iqr_ranges.csv")
# descriptive_statistics.generate_quantiles_report(statistics_data, "quantiles_01.csv", 0.1)
# descriptive_statistics.generate_quantiles_report(statistics_data, "quantiles_09.csv", 0.9)
# print('Generated statistics reports.')
#
# descriptive_statistics.get_outliers_report(statistics_data, "outliers.csv")
# descriptive_statistics.get_outliers_counters_report(statistics_data, "outliers_counters.csv")
# descriptive_statistics.get_pearson_attributes_correlation_report(statistics_data, "pearson_attributes_correlation.csv")
# descriptive_statistics.get_pearson_class_correlation_report(statistics_data, "pearson_class_correlation.csv",
#                                                             class_column)
# descriptive_statistics.get_linear_regression_report(statistics_data, "radius_mean", "symmetry_mean",
#                                                     "radius_symmetry_mean_regression.csv")
# descriptive_statistics.get_linear_regression_report(statistics_data, "texture_mean", "smoothness_mean",
#                                                     "texture_smoothness_mean_regression.csv")
#
# visualisation_data = data_preparer.get_data_for_visualisation(raw_data)
# visualizator.create_attributes_values_diagram(visualisation_data)
# visualizator.create_histograms(visualisation_data)
# visualizator.create_linear_regression_diagram(visualisation_data, "radius_mean", "symmetry_mean")
# visualizator.create_linear_regression_diagram(visualisation_data, "texture_mean", "smoothness_mean")
# visualizator.create_box_diagrams(visualisation_data)

classification_data = data_preparer.get_data_with_filled_gaps(raw_data)
random_forest.classify(classification_data)
# random_forest.classify_kfold(classification_data, 50)
