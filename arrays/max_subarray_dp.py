def max_subarray_dp(nums):
    """
    Find maximum subarray sum using DP table (O(n) time, O(n) space)
    """
    if not nums:
        return 0

    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    max_sum = dp[0]

    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
        max_sum = max(max_sum, dp[i])

    return max_sum

# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_dp(nums)
print(f"DP result: {result}")  # 6
