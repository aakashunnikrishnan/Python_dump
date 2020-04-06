def merge_dicts_union(dict1, dict2):
    """Using the | operator with custom merging (Python 3.9+)"""
    # This doesn't sum values, but we can create a custom approach
    return {key: dict1.get(key, 0) + dict2.get(key, 0)
            for key in set(dict1) | set(dict2)}

# Example
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 1, 'd': 4}
result = merge_dicts_union(dict1, dict2)
print(result)  # {'a': 1, 'b': 5, 'c': 4, 'd': 4}
