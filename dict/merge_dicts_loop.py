def merge_dicts_loop(dict1, dict2):
    """Merge using copy and loop"""
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value

    return result

# Example
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 1, 'd': 4}
result = merge_dicts_loop(dict1, dict2)
print(result)  # {'a': 1, 'b': 5, 'c': 4, 'd': 4}
