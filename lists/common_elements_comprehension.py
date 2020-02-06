def common_elements_comprehension(list1, list2):
    """Find common elements while preserving order from list1"""
    set2 = set(list2)
    return [x for x in list1 if x in set2]

# Example
list1 = [1, 2, 3, 4, 5, 6, 1, 2]
list2 = [4, 5, 6, 7, 8, 9]
result = common_elements_comprehension(list1, list2)
print(result)  # [4, 5, 6, 4, 5, 6] - includes duplicates from list1
