def remove_every_nth_inplace(lst, n):
    """Remove every nth element in-place (modifies original list)"""
    if n <= 0:
        return lst

    # Remove from end to start to avoid index shifting issues
    for i in range(len(lst) - 1, -1, -1):
        if (i + 1) % n == 0:
            del lst[i]

    return lst

# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_every_nth_inplace(numbers.copy(), 3)
print(result)  # [1, 2, 4, 5, 7, 8, 10]
