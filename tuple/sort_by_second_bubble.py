def sort_by_second_bubble(tuples_list):
    """Sort using bubble sort (for learning purposes)"""
    arr = tuples_list.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Example
tuples = [(1, 2), (3, 1), (5, 0)]
result = sort_by_second_bubble(tuples)
print(result)  # [(5, 0), (3, 1), (1, 2)]
