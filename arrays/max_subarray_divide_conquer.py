def max_subarray_divide_conquer(nums):
    """
    Find maximum subarray sum using divide and conquer
    """
    if not nums:
        return 0

    def max_crossing_sum(arr, left, mid, right):
        # Find max sum crossing to the left
        left_sum = float('-inf')
        sum_val = 0
        for i in range(mid, left - 1, -1):
            sum_val += arr[i]
            left_sum = max(left_sum, sum_val)

        # Find max sum crossing to the right
        right_sum = float('-inf')
        sum_val = 0
        for i in range(mid + 1, right + 1):
            sum_val += arr[i]
            right_sum = max(right_sum, sum_val)

        return left_sum + right_sum

    def max_subarray_recursive(arr, left, right):
        if left == right:
            return arr[left]

        mid = (left + right) // 2

        left_max = max_subarray_recursive(arr, left, mid)
        right_max = max_subarray_recursive(arr, mid + 1, right)
        cross_max = max_crossing_sum(arr, left, mid, right)

        return max(left_max, right_max, cross_max)

    return max_subarray_recursive(nums, 0, len(nums) - 1)

# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_divide_conquer(nums)
print(f"Divide & conquer result: {result}")  # 6
