def remove_every_nth_filter(lst, n):
    """Remove every nth element using filter"""
    if n <= 0:
        return lst

    return list(filter(lambda x: x[0] % n != 0, enumerate(lst, 1)))

# Or more clearly:
def remove_every_nth_filter_clear(lst, n):
    if n <= 0:
        return lst

    return [item for item in lst if (lst.index(item) + 1) % n != 0]

# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_every_nth_filter_clear(numbers, 3)
print(result)  # [1, 2, 4, 5, 7, 8, 10]
