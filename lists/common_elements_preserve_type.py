def common_elements_preserve_type(list1, list2):
    """Find common elements while preserving original type if possible"""
    result = set(list1) & set(list2)

    # Try to preserve original type (if list contains same type)
    if result and all(isinstance(x, type(next(iter(result)))) for x in result):
        return sorted(result) if isinstance(list1[0], (int, float)) else list(result)
    return list(result)

# Example
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = common_elements_preserve_type(list1, list2)
print(result)  # [4, 5]
