from itertools import compress, cycle

def remove_every_nth_compress(lst, n):
    """Remove every nth element using itertools.compress"""
    if n <= 0:
        return lst

    # Create a selector: True for elements to keep, False for nth element
    # Pattern: n-1 Trues, 1 False, repeat
    selector = cycle([True] * (n - 1) + [False])

    return list(compress(lst, selector))

# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_every_nth_compress(numbers, 3)
print(result)  # [1, 2, 4, 5, 7, 8, 10]
