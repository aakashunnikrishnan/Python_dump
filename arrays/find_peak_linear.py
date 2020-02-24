def find_peak_linear(nums):
    """Find any peak element using linear scan"""
    if not nums:
        return None

    n = len(nums)

    # Check first element
    if n == 1 or nums[0] > nums[1]:
        return 0

    # Check middle elements
    for i in range(1, n - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i

    # Check last element
    if nums[-1] > nums[-2]:
        return n - 1

    return None

# Example
numbers = [1, 2, 3, 1]
result = find_peak_linear(numbers)
print(f"Peak found at index {result}, value: {numbers[result]}")  # Index 2, value 3
