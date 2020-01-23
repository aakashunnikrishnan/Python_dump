def rotate_left_comprehension(lst, k):
    """Rotate left using list comprehension with modulo indexing"""
    if not lst:
        return lst

    n = len(lst)
    k = k % n

    return [lst[(i + k) % n] for i in range(n)]

# Example
original = [1, 2, 3, 4, 5]
result = rotate_left_comprehension(original, 2)
print(result)  # [3, 4, 5, 1, 2]
