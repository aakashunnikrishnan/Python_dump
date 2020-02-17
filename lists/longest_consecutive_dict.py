def longest_consecutive_dict(nums):
    """Find longest consecutive sequence using dictionary"""
    if not nums:
        return 0

    num_dict = {}
    longest = 0

    for num in nums:
        if num not in num_dict:
            left = num_dict.get(num - 1, 0)
            right = num_dict.get(num + 1, 0)

            current_length = left + right + 1
            longest = max(longest, current_length)

            # Update the boundaries
            num_dict[num] = current_length
            num_dict[num - left] = current_length
            num_dict[num + right] = current_length

    return longest

# Example
numbers = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_dict(numbers)
print(result)  # 4
