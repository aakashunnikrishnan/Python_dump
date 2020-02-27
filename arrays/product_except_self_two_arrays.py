def product_except_self_two_arrays(nums):
    """Using separate left and right arrays for clarity"""
    n = len(nums)

    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n

    # Fill left_products
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    # Fill right_products
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    # Combine
    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result

# Example
nums = [1, 2, 3, 4]
result = product_except_self_two_arrays(nums)
print(result)  # [24, 12, 8, 6]
