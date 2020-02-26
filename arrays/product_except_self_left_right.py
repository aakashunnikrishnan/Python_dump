def product_except_self_left_right(nums):
    """Calculate product of all elements except self using left and right products"""
    n = len(nums)

    # Initialize result array with 1's
    result = [1] * n

    # Calculate left products (products of all elements to the left)
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Calculate right products and multiply with left products
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

# Example
nums = [1, 2, 3, 4]
result = product_except_self_left_right(nums)
print(result)  # [24, 12, 8, 6]
