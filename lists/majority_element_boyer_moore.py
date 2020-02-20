def majority_element_boyer_moore(nums):
    """
    Find majority element using Boyer-Moore Voting Algorithm
    Returns the element if it exists, otherwise None
    """
    if not nums:
        return None

    # Phase 1: Find candidate
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Phase 2: Verify candidate is actually majority
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None

# Example
numbers = [3, 3, 4, 2, 3, 3, 3, 1, 3]
result = majority_element_boyer_moore(numbers)
print(result)  # 3
