def longest_consecutive_sort(nums):
    """Find longest consecutive sequence by sorting first"""
    if not nums:
        return 0
    
    nums_sorted = sorted(set(nums))  # Use set to remove duplicates
    longest = 1
    current_length = 1
    
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] == nums_sorted[i-1] + 1:
            current_length += 1
            longest = max(longest, current_length)
        else:
            current_length = 1
    
    return longest

# Example
numbers = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_sort(numbers)
print(result)  # 4
