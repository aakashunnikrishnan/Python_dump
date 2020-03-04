def is_mountain_array_max(arr):
    """Check mountain array using max element and split"""
    if len(arr) < 3:
        return False

    # Find the peak (maximum element)
    peak_index = arr.index(max(arr))

    # Peak can't be at ends
    if peak_index == 0 or peak_index == len(arr) - 1:
        return False

    # Check strictly increasing to peak
    for i in range(peak_index):
        if arr[i] >= arr[i + 1]:
            return False

    # Check strictly decreasing after peak
    for i in range(peak_index, len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            return False

    return True

# Example
arr1 = [1, 2, 3, 2, 1]
arr2 = [1, 2, 2, 2, 1]  # Not strictly increasing/decreasing
print(is_mountain_array_max(arr1))  # True
print(is_mountain_array_max(arr2))  # False
