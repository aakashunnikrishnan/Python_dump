def majority_element_sort(nums):
    """Find majority element by sorting"""
    if not nums:
        return None

    nums_sorted = sorted(nums)
    candidate = nums_sorted[len(nums) // 2]

    # Verify
    if nums_sorted.count(candidate) > len(nums) // 2:
        return candidate
    return None

# Example
numbers = [3, 3, 4, 2, 3, 3, 3, 1, 3]
result = majority_element_sort(numbers)
print(result)  # 3
