def move_zeroes_partition(lst):
    """Partition the list with zeroes at the end"""
    # Create a list of indices where element is non-zero
    non_zero_indices = [i for i, x in enumerate(lst) if x != 0]

    # Create result list
    result = [lst[i] for i in non_zero_indices]
    result.extend([0] * (len(lst) - len(non_zero_indices)))
    return result

# Example
numbers = [0, 1, 0, 3, 0, 12, 0, 5]
result = move_zeroes_partition(numbers)
print(result)  # [1, 3, 12, 5, 0, 0, 0, 0]
