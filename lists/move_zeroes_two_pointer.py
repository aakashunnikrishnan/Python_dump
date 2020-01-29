def move_zeroes_two_pointer(lst):
    """Move zeroes to end using two pointers (in-place, O(n))"""
    non_zero_pos = 0

    # Move all non-zero elements to the front
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[non_zero_pos], lst[i] = lst[i], lst[non_zero_pos]
            non_zero_pos += 1

    return lst

# Example
numbers = [0, 1, 0, 3, 0, 12, 0, 5]
result = move_zeroes_two_pointer(numbers.copy())
print(result)  # [1, 3, 12, 5, 0, 0, 0, 0]
