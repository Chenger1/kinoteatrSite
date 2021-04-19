def get_valid_dir_name(instance_name):
    symbols = {'/', '\\', ':', '?', '"', '<', '>', '|'}
    intersection = set(instance_name) & symbols
    if intersection:
        for symbol in intersection:
            instance_name = instance_name.replace(symbol, '_')
    return instance_name
