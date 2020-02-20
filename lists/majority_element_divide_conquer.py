def majority_element_divide_conquer(nums):
    """Find majority element using divide and conquer"""
    if not nums:
        return None

    def majority_recursive(left, right):
        if left == right:
            return nums[left]

        mid = (left + right) // 2
        left_majority = majority_recursive(left, mid)
        right_majority = majority_recursive(mid + 1, right)

        if left_majority == right_majority:
            return left_majority

        # Count occurrences of both candidates
        left_count = sum(1 for i in range(left, right + 1) if nums[i] == left_majority)
        right_count = sum(1 for i in range(left, right + 1) if nums[i] == right_majority)

        return left_majority if left_count > right_count else right_majority

    candidate = majority_recursive(0, len(nums) - 1)

    # Verify candidate
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None

# Example
numbers = [3, 3, 4, 2, 3, 3, 3, 1, 3]
result = majority_element_divide_conquer(numbers)
print(result)  # 3
