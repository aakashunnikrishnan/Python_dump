def max_subarray_bruteforce(nums):
    """
    Find maximum subarray sum using brute force (O(n²))
    """
    if not nums:
        return 0

    n = len(nums)
    max_sum = float('-inf')

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

    return max_sum

# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_bruteforce(nums)
print(f"Brute force result: {result}")  # 6
