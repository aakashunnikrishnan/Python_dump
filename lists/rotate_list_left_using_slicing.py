def rotate_left_slicing(lst, k):
    """Rotate left using list slicing"""
    if not lst:
        return lst

    # Handle k > len(lst) by taking modulo
    k = k % len(lst)

    # Slice and concatenate
    return lst[k:] + lst[:k]

# Example
original = [1, 2, 3, 4, 5]
result = rotate_left_slicing(original, 2)
print(result)  # [3, 4, 5, 1, 2]
