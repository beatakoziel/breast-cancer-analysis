def get_data_with_filled_gaps(data):
    data.radius_mean.fillna(data.radius_mean.mean(), inplace=True)
    data.texture_mean.fillna(data.texture_mean.mean(), inplace=True)
    data.perimeter_mean.fillna(data.perimeter_mean.mean(), inplace=True)
    data.area_mean.fillna(data.area_mean.mean(), inplace=True)
    data.smoothness_mean.fillna(data.smoothness_mean.mean(), inplace=True)
    data.compactness_mean.fillna(data.compactness_mean.mean(), inplace=True)
    data.concavity_mean.fillna(data.concavity_mean.mean(), inplace=True)
    data.concave_points_mean.fillna(data.concave_points_mean.mean(), inplace=True)
    data.symmetry_mean.fillna(data.symmetry_mean.mean(), inplace=True)
    data.fractal_dimension_mean.fillna(data.fractal_dimension_mean.mean(), inplace=True)
    data.radius_se.fillna(data.radius_se.mean(), inplace=True)
    data.texture_se.fillna(data.texture_se.mean(), inplace=True)
    data.perimeter_se.fillna(data.perimeter_se.mean(), inplace=True)
    data.area_se.fillna(data.area_se.mean(), inplace=True)
    data.smoothness_se.fillna(data.smoothness_se.mean(), inplace=True)
    data.compactness_se.fillna(data.compactness_se.mean(), inplace=True)
    data.concavity_se.fillna(data.concavity_se.mean(), inplace=True)
    data.concave_points_se.fillna(data.concave_points_se.mean(), inplace=True)
    data.symmetry_se.fillna(data.symmetry_se.mean(), inplace=True)
    data.fractal_dimension_se.fillna(data.fractal_dimension_se.mean(), inplace=True)
    data.radius_worst.fillna(data.radius_worst.mean(), inplace=True)
    data.texture_worst.fillna(data.texture_worst.mean(), inplace=True)
    data.perimeter_worst.fillna(data.perimeter_worst.mean(), inplace=True)
    data.area_worst.fillna(data.area_worst.mean(), inplace=True)
    data.smoothness_worst.fillna(data.smoothness_worst.mean(), inplace=True)
    data.compactness_worst.fillna(data.compactness_worst.mean(), inplace=True)
    data.concavity_worst.fillna(data.concavity_worst.mean(), inplace=True)
    data.concave_points_worst.fillna(data.concave_points_worst.mean(), inplace=True)
    data.symmetry_worst.fillna(data.symmetry_worst.mean(), inplace=True)
    data.fractal_dimension_worst.fillna(data.fractal_dimension_worst.mean(), inplace=True)
    return data


def get_class_column(data):
    return data.diagnosis


def get_data_for_statistics(data):
    data.drop(["id", "diagnosis"], axis=1, inplace=True)
    return data
