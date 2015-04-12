def transform(old_style):
    return_value = {}
    for key, value_list in old_style.items():
        for value in value_list:
            return_value[value.lower()] = key

    return return_value
