from collections import deque

def move_zeroes_deque(lst):
    """Use deque to efficiently move zeroes"""
    non_zero = deque()
    zero_count = 0

    for num in lst:
        if num == 0:
            zero_count += 1
        else:
            non_zero.append(num)

    non_zero.extend([0] * zero_count)
    return list(non_zero)

# Example
numbers = [0, 1, 0, 3, 0, 12, 0, 5]
result = move_zeroes_deque(numbers)
print(result)  # [1, 3, 12, 5, 0, 0, 0, 0]
