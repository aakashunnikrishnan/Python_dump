def max_subarray_kadane(nums):
    """
    Find maximum subarray sum using Kadane's algorithm
    Returns the sum of the contiguous subarray with largest sum
    """
    if not nums:
        return 0

    max_so_far = nums[0]
    max_ending_here = nums[0]

    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_kadane(nums)
print(f"Maximum subarray sum: {result}")  # 6 (subarray: [4, -1, 2, 1])
