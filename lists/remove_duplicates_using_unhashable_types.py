def remove_duplicates_unhashable(lst):
    """Works for unhashable types like lists and dicts"""
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# Example with unhashable types
unhashable_list = [
    [1, 2],
    {'a': 1},
    [1, 2],
    {'b': 2},
    [3, 4],
    {'a': 1}
]

result = remove_duplicates_unhashable(unhashable_list)
print(f"Unhashable types: {unhashable_list}")
print(f"After removal: {result}")
