def move_zeroes_count(lst):
    """Count zeroes, remove them, then append zeroes"""
    zero_count = lst.count(0)
    result = [x for x in lst if x != 0]
    result.extend([0] * zero_count)
    return result

# Example
numbers = [0, 1, 0, 3, 0, 12, 0, 5]
result = move_zeroes_count(numbers)
print(result)  # [1, 3, 12, 5, 0, 0, 0, 0]
