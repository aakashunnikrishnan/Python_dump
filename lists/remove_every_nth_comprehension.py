def remove_every_nth_comprehension(lst, n):
    """Remove every nth element using list comprehension"""
    if n <= 0:
        return lst

    return [item for i, item in enumerate(lst, 1) if i % n != 0]

# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_every_nth_comprehension(numbers, 3)
print(result)  # [1, 2, 4, 5, 7, 8, 10]
