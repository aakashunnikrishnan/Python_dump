def remove_every_nth_slice(lst, n):
    """Remove every nth element using slicing"""
    if n <= 0:
        return lst

    result = []
    for i in range(0, len(lst), n):
        # Add elements before the nth element
        result.extend(lst[i:i + n - 1])

    return result

# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_every_nth_slice(numbers, 3)
print(result)  # [1, 2, 4, 5, 7, 8, 10]
