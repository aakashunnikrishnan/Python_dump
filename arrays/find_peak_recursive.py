def find_peak_recursive(nums, left=None, right=None):
    """Find peak using recursive binary search"""
    if not nums:
        return None

    if left is None:
        left = 0
    if right is None:
        right = len(nums) - 1

    if left == right:
        return left

    mid = (left + right) // 2

    if nums[mid] > nums[mid + 1]:
        return find_peak_recursive(nums, left, mid)
    else:
        return find_peak_recursive(nums, mid + 1, right)

# Example
numbers = [1, 2, 3, 1]
result = find_peak_recursive(numbers)
print(f"Peak found at index {result}, value: {numbers[result]}")
