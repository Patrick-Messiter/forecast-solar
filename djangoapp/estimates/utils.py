def convert_floats_to_ints_if_whole(value):
    return int(value) if isinstance(value, float) and value.is_integer() else value