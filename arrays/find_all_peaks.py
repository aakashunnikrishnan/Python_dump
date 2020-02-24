def find_all_peaks(nums):
    """Find all peak elements in the list"""
    if not nums:
        return []

    n = len(nums)
    peaks = []

    # Check first element
    if n == 1 or nums[0] > nums[1]:
        peaks.append(0)

    # Check middle elements
    for i in range(1, n - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            peaks.append(i)

    # Check last element
    if n > 1 and nums[-1] > nums[-2]:
        peaks.append(n - 1)

    return peaks

# Example
numbers = [1, 3, 2, 5, 4, 6, 1]
result = find_all_peaks(numbers)
print(f"All peaks at indices: {result}, values: {[numbers[i] for i in result]}")
