def first_repeating_comprehension(arr):
    """Find first repeating element using list comprehension (O(n²))"""
    for i, num in enumerate(arr):
        if num in arr[i+1:]:
            return num
    return None

# Example
arr = [10, 5, 3, 4, 3, 5, 6]
result = first_repeating_comprehension(arr)
print(f"First repeating element: {result}")  # 3
