def product_except_self_prefix_suffix(nums):
    """Using prefix and suffix products"""
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n

    # Prefix products (product of all elements before i)
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    # Suffix products (product of all elements after i)
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    # Combine
    return [prefix[i] * suffix[i] for i in range(n)]

# Example
nums = [1, 2, 3, 4]
result = product_except_self_prefix_suffix(nums)
print(result)  # [24, 12, 8, 6]
