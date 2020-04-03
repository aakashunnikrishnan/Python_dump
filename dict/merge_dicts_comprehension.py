def merge_dicts_comprehension(dict1, dict2):
    """Merge two dictionaries, summing values for common keys"""
    all_keys = set(dict1.keys()) | set(dict2.keys())
    return {key: dict1.get(key, 0) + dict2.get(key, 0) for key in all_keys}

# Example
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 1, 'd': 4}
result = merge_dicts_comprehension(dict1, dict2)
print(result)  # {'a': 1, 'b': 5, 'c': 4, 'd': 4}
