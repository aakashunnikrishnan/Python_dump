def majority_element_bit_manipulation(nums):
    """Find majority element using bit manipulation (for integers only)"""
    if not nums:
        return None

    n = len(nums)
    majority = 0

    # Check each bit position (assuming 32-bit integers)
    for bit in range(32):
        count = 0
        for num in nums:
            if num & (1 << bit):
                count += 1

        if count > n // 2:
            majority |= (1 << bit)

    # Verify candidate (handles negative numbers)
    if nums.count(majority) > n // 2:
        return majority
    return None

# Example
numbers = [3, 3, 4, 2, 3, 3, 3, 1, 3]
result = majority_element_bit_manipulation(numbers)
print(result)  # 3
