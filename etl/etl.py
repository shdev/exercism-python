def transform(old_style):
    return {value.lower(): key
            for key, value_list in old_style.items()
            for value in value_list}
