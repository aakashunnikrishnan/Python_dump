def find_peak_binary_search(nums):
    """Find a peak element using binary search (O(log n))"""
    if not nums:
        return None

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            # Peak is on the left side (including mid)
            right = mid
        else:
            # Peak is on the right side
            left = mid + 1

    return left

# Example
numbers = [1, 2, 3, 1]
result = find_peak_binary_search(numbers)
print(f"Peak found at index {result}, value: {numbers[result]}")  # Index 2, value 3
