def is_mountain_array_two_pointer(arr):
    """Check if array is a mountain array using two pointers"""
    if len(arr) < 3:
        return False

    left = 0
    right = len(arr) - 1

    # Walk up from left while strictly increasing
    while left + 1 < len(arr) and arr[left] < arr[left + 1]:
        left += 1

    # Walk down from right while strictly decreasing
    while right - 1 >= 0 and arr[right] < arr[right - 1]:
        right -= 1

    # If left and right meet at the same position (peak) and it's not at ends
    return left == right and left != 0 and right != len(arr) - 1

# Example
arr1 = [1, 2, 3, 2, 1]
arr2 = [1, 2, 3, 4, 5]
arr3 = [5, 4, 3, 2, 1]

print(is_mountain_array_two_pointer(arr1))  # True
print(is_mountain_array_two_pointer(arr2))  # False (strictly increasing)
print(is_mountain_array_two_pointer(arr3))  # False (strictly decreasing)
