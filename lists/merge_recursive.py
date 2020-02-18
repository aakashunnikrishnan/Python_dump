def merge_recursive(list1, list2):
    """Merge two sorted lists recursively"""
    if not list1:
        return list2
    if not list2:
        return list1

    if list1[0] <= list2[0]:
        return [list1[0]] + merge_recursive(list1[1:], list2)
    else:
        return [list2[0]] + merge_recursive(list1, list2[1:])

# Example
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = merge_recursive(list1, list2)
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8]
