def rotate_left_loop(lst, k):
    """Rotate left using a loop and pop/append"""
    if not lst:
        return lst

    # Create a copy to avoid modifying original
    result = lst.copy()
    k = k % len(result)

    for _ in range(k):
        # Remove first element and append it to the end
        result.append(result.pop(0))

    return result

# Example
original = [1, 2, 3, 4, 5]
result = rotate_left_loop(original, 2)
print(result)  # [3, 4, 5, 1, 2]
