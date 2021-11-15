def get_data_with_filled_gaps(data):
    data = get_data_without_symbols(data)
    for col in data.columns:
        data[col].fillna(data[col].mean().round(3), inplace=True)
    return data


def get_data_without_symbols(data):
    data['diagnosis'] = data['diagnosis'].replace({'M': 1})
    data['diagnosis'] = data['diagnosis'].replace({'B': 0})
    return data


def get_class_column(data):
    data = get_data_without_symbols(data)
    return data.diagnosis


def get_data_for_statistics(data):
    data = get_data_with_filled_gaps(data)
    data.drop(["id", "diagnosis"], axis=1, inplace=True)
    return data


def get_data_for_visualisation(data):
    data.drop(
        ["radius_se", "texture_se", "perimeter_se", "area_se", "smoothness_se", "compactness_se",
         "concavity_se", "concave_points_se", "symmetry_se", "fractal_dimension_se", "radius_worst", "texture_worst",
         "perimeter_worst", "area_worst", "smoothness_worst", "compactness_worst", "concavity_worst",
         "concave_points_worst", "symmetry_worst", "fractal_dimension_worst"], axis=1, inplace=True)
    return data
