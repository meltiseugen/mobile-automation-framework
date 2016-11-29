import json


def generate_key(collection, key):
    """
    Generator for values of a certain key.
    EXAMPLE:
    for k in generate_key(d, "c"):
        print(k)
    :param dictionary: the dictionary to be parsed.
    :param key: the key searched for.
    :return:
    """
    for k in collection:
        if k == key:
            yield collection[k]
        if isinstance(k, dict):
            yield from filter_key(k, key)
        elif isinstance(k, list):
            for list_item in k:
                yield from filter_key(k, list_item)
        elif isinstance(collection, list) and isinstance(k, str):
            pass
        elif isinstance(collection[k], list):
            yield from filter_key(collection[k], key)
        elif isinstance(collection[k], dict):
            yield from filter_key(collection[k], key)
        elif k == key and isinstance(collection[k], dict):
            yield from filter_key(collection[k], key)


def filter_key(collection, key):
    """
    Filter a dictionary for a certain key.
    EXAMPLE:
    print(filter_key(d, "1"))
    :param collection: dictionary or list
    :param dictionary: the dictionary.
    :param key: the key
    :return: returns a list of values.
    """
    results = []
    for k in collection:
        if k == key:
            results.append(collection[k])
        if isinstance(k, dict):
            results.extend(filter_key(k, key))
        elif isinstance(k, list):
            for list_item in k:
                results.extend(filter_key(k, list_item))
        elif isinstance(collection, list) and isinstance(k, str):
            pass
        elif isinstance(collection[k], list):
            results.extend(filter_key(collection[k], key))
        elif isinstance(collection[k], dict):
            results.extend((filter_key(collection[k], key)))
        elif k == key and isinstance(collection[k], dict):
            results.extend(filter_key(collection[k], key))
    return results


def filter_by_keys(collection, keys_list):
    result = {}
    for key in keys_list:
        result[key] = filter_key(collection, key)
    return result
