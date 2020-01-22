def remove_duplicates_enumerate(lst):
    """Uses enumerate to check first occurrence index"""
    return [item for i, item in enumerate(lst) if lst.index(item) == i]

# Example
original = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
result = remove_duplicates_enumerate(original)
print(result)  # [1, 2, 3, 4, 5, 6]
