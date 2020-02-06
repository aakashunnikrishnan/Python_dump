def common_elements_loop(list1, list2):
    """Find common elements using nested loops (simple but inefficient)"""
    common = []
    set2 = set(list2)  # Convert to set for O(1) lookup

    for item in list1:
        if item in set2 and item not in common:
            common.append(item)

    return common

# Example
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
result = common_elements_loop(list1, list2)
print(result)  # [4, 5, 6]
