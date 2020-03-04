def is_mountain_array_single_pass(arr):
    """Check mountain array by finding peak and verifying"""
    if len(arr) < 3:
        return False

    # Find the peak (where increasing stops)
    i = 0
    n = len(arr)

    # Walk up while strictly increasing
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    # Peak can't be first or last element
    if i == 0 or i == n - 1:
        return False

    # Walk down while strictly decreasing
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    # If we reached the end, it's a valid mountain
    return i == n - 1

# Example
arr1 = [1, 2, 3, 2, 1]
arr2 = [1, 2, 3, 4, 5]
print(is_mountain_array_single_pass(arr1))  # True
print(is_mountain_array_single_pass(arr2))  # False
