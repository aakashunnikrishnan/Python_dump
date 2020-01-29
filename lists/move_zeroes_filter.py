def move_zeroes_filter(lst):
    """Move zeroes by filtering non-zero elements and appending zeroes"""
    non_zero = [x for x in lst if x != 0]
    zero_count = len(lst) - len(non_zero)
    return non_zero + [0] * zero_count

# Example
numbers = [0, 1, 0, 3, 0, 12, 0, 5]
result = move_zeroes_filter(numbers)
print(result)  # [1, 3, 12, 5, 0, 0, 0, 0]
