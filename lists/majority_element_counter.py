from collections import Counter

def majority_element_counter(nums):
    """Find majority element using Counter"""
    if not nums:
        return None

    counts = Counter(nums)
    majority_count = len(nums) // 2

    for num, count in counts.items():
        if count > majority_count:
            return num

    return None

# Example
numbers = [3, 3, 4, 2, 3, 3, 3, 1, 3]
result = majority_element_counter(numbers)
print(result)  # 3
