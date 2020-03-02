def first_repeating_dict_index(arr):
    """Find first repeating element using dictionary to track indices"""
    index_map = {}
    first_repeat_index = float('inf')
    first_repeat_value = None

    for i, num in enumerate(arr):
        if num in index_map:
            # Found a repeat, check if this is earlier than previous repeat
            if index_map[num] < first_repeat_index:
                first_repeat_index = index_map[num]
                first_repeat_value = num
        else:
            index_map[num] = i

    return first_repeat_value

# Example
arr = [10, 5, 3, 4, 3, 5, 6]
result = first_repeating_dict_index(arr)
print(f"First repeating element (by first occurrence): {result}")  # 3
