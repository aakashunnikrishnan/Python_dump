def longest_consecutive_bruteforce(nums):
    """Find longest consecutive sequence using brute force (inefficient)"""
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in nums:
        current_length = 1
        current_num = num

        while current_num + 1 in num_set:
            current_num += 1
            current_length += 1

        longest = max(longest, current_length)

    return longest

# Example
numbers = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_bruteforce(numbers)
print(result)  # 4
