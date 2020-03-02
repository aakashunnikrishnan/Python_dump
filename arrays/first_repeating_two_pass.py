def first_repeating_two_pass(arr):
    """Find first repeating element using two-pass approach"""
    seen = set()
    repeats = set()

    # First pass: find all elements that repeat
    for num in arr:
        if num in seen:
            repeats.add(num)
        seen.add(num)

    # Second pass: find first element that's in repeats
    for num in arr:
        if num in repeats:
            return num

    return None

# Example
arr = [10, 5, 3, 4, 3, 5, 6]
result = first_repeating_two_pass(arr)
print(f"First repeating element: {result}")  # 3
