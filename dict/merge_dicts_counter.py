from collections import Counter

def merge_dicts_counter(dict1, dict2):
    """Merge using Counter (works best for numeric values)"""
    return dict(Counter(dict1) + Counter(dict2))

# Example
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 1, 'd': 4}
result = merge_dicts_counter(dict1, dict2)
print(result)  # {'a': 1, 'b': 5, 'c': 4, 'd': 4}
