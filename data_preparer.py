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
    return data.diagnosis


def get_data_for_statistics(data):
    data = get_data_with_filled_gaps(data)
    data.drop(["id", "diagnosis"], axis=1, inplace=True)
    return data
