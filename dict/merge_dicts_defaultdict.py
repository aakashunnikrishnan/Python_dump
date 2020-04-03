from collections import defaultdict

def merge_dicts_defaultdict(dict1, dict2):
    """Merge using defaultdict"""
    result = defaultdict(int)

    for key, value in dict1.items():
        result[key] += value

    for key, value in dict2.items():
        result[key] += value

    return dict(result)

# Example
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 1, 'd': 4}
result = merge_dicts_defaultdict(dict1, dict2)
print(result)  # {'a': 1, 'b': 5, 'c': 4, 'd': 4}
