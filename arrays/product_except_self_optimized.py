def product_except_self_optimized(nums):
    """O(1) extra space solution using the result array for left products"""
    n = len(nums)
    result = [1] * n

    # Store left products in result array
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    # Multiply with right products
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

# Example
nums = [1, 2, 3, 4]
result = product_except_self_optimized(nums)
print(result)  # [24, 12, 8, 6]
