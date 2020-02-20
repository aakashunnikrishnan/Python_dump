def majority_element_dict(nums):
    """Find majority element using manual dictionary"""
    if not nums:
        return None

    freq = {}
    majority_threshold = len(nums) // 2

    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > majority_threshold:
            return num

    return None

# Example
numbers = [3, 3, 4, 2, 3, 3, 3, 1, 3]
result = majority_element_dict(numbers)
print(result)  # 3
