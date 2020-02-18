def merge_two_pointers(list1, list2):
    """Merge two sorted lists using two pointers (in-place style)"""
    merged = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Add remaining elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged

# Example
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = merge_two_pointers(list1, list2)
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8]
