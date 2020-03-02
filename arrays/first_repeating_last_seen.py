def first_repeating_last_seen(arr):
    """Find first repeating element by storing last seen position"""
    last_seen = {}
    min_index = float('inf')
    result = None

    for i, num in enumerate(arr):
        if num in last_seen:
            if last_seen[num] < min_index:
                min_index = last_seen[num]
                result = num
        else:
            last_seen[num] = i

    return result

# Example
arr = [10, 5, 3, 4, 3, 5, 6]
result = first_repeating_last_seen(arr)
print(f"First repeating element: {result}")  # 3
