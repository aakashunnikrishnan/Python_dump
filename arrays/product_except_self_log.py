import math

def product_except_self_log(nums):
    """Using logarithms (NOT recommended for production due to precision)"""
    n = len(nums)

    # Handle zeros
    if any(x == 0 for x in nums):
        return product_except_self_with_zeros(nums)

    log_sum = sum(math.log(abs(x)) for x in nums)

    result = []
    for num in nums:
        sign = 1
        if (sum(1 for x in nums if x < 0) - (1 if num < 0 else 0)) % 2 == 1:
            sign = -1

        prod = math.exp(log_sum - math.log(abs(num)))
        result.append(sign * round(prod))

    return result

# Example
nums = [1, 2, 3, 4]
result = product_except_self_log(nums)
print(result)  # [24, 12, 8, 6]
