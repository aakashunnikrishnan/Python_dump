def longest_consecutive_set(nums):
    """Find longest consecutive sequence using set (O(n) time)"""
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting if it's the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            longest = max(longest, current_length)

    return longest

# Example
numbers = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_set(numbers)
print(result)  # 4 (sequence: 1,2,3,4)
