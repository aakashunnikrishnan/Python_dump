def merge_extend_sort(list1, list2):
    """Merge by extending then sorting"""
    result = list1.copy()
    result.extend(list2)
    result.sort()
    return result

# Example
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = merge_extend_sort(list1, list2)
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8]
