def max_subarray_with_indices(nums):
    """
    Find maximum subarray sum AND return the subarray
    """
    if not nums:
        return 0, []

    max_so_far = nums[0]
    max_ending_here = nums[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > max_ending_here + nums[i]:
            # Start new subarray
            max_ending_here = nums[i]
            temp_start = i
        else:
            # Extend current subarray
            max_ending_here = max_ending_here + nums[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i

    return max_so_far, nums[start:end+1]

# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sum_val, subarray = max_subarray_with_indices(nums)
print(f"Maximum sum: {sum_val}, Subarray: {subarray}")  # 6, [4, -1, 2, 1]
