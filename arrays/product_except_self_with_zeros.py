def product_except_self_with_zeros(nums):
    """Handle arrays containing zeros"""
    n = len(nums)
    zero_count = 0
    total_product = 1

    # Count zeros and compute total product (excluding zeros)
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            total_product *= num

    result = [0] * n

    for i in range(n):
        if zero_count > 1:
            # More than one zero, all products are 0
            result[i] = 0
        elif zero_count == 1:
            # Exactly one zero
            if nums[i] == 0:
                result[i] = total_product
            else:
                result[i] = 0
        else:
            # No zeros
            result[i] = total_product // nums[i]  # Using division, but only without zeros

    return result

# Example with zeros
nums = [1, 2, 0, 4]
result = product_except_self_with_zeros(nums)
print(result)  # [0, 0, 8, 0]
