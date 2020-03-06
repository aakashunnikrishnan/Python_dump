def max_subarray_cumulative(nums):
    """
    Find maximum subarray sum using cumulative sums
    """
    if not nums:
        return 0

    min_prefix = 0
    max_sum = float('-inf')
    prefix_sum = 0

    for num in nums:
        prefix_sum += num
        max_sum = max(max_sum, prefix_sum - min_prefix)
        min_prefix = min(min_prefix, prefix_sum)

    return max_sum

# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_cumulative(nums)
print(f"Cumulative sums result: {result}")  # 6
