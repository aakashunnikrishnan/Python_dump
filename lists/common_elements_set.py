def common_elements_set(list1, list2):
    """Find common elements using set intersection"""
    return list(set(list1) & set(list2))

# Example
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
result = common_elements_set(list1, list2)
print(result)  # [4, 5, 6]
