def common_elements_filter(list1, list2):
    """Find common elements using filter"""
    set2 = set(list2)
    return list(filter(lambda x: x in set2, list1))

# Example
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
result = common_elements_filter(list1, list2)
print(result)  # [4, 5, 6]
