def first_repeating_set(arr):
    """Find first repeating element using a set"""
    seen = set()

    for num in arr:
        if num in seen:
            return num
        seen.add(num)

    return None  # No repeating element

# Example
arr = [10, 5, 3, 4, 3, 5, 6]
result = first_repeating_set(arr)
print(f"First repeating element: {result}")  # 3
