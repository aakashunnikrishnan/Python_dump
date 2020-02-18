def merge_inplace(list1, list2, m, n):
    """
    Merge list2 into list1 assuming list1 has extra space at end
    list1: has length m+n with first m elements sorted
    list2: has length n sorted
    """
    i = m - 1  # Last element in list1's valid portion
    j = n - 1  # Last element in list2
    k = m + n - 1  # Last position in list1

    while i >= 0 and j >= 0:
        if list1[i] >= list2[j]:
            list1[k] = list1[i]
            i -= 1
        else:
            list1[k] = list2[j]
            j -= 1
        k -= 1

    # Copy remaining elements from list2 (if any)
    while j >= 0:
        list1[k] = list2[j]
        j -= 1
        k -= 1

    return list1

# Example
list1 = [1, 3, 5, 7, 0, 0, 0, 0]  # Extra space at end
list2 = [2, 4, 6, 8]
result = merge_inplace(list1, list2, 4, 4)
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8]
