def sort_by_second_custom(tuples_list):
    """Sort using a custom comparison function (Python 2 style)"""
    # In Python 3, we need to use key or cmp_to_key
    from functools import cmp_to_key

    def compare(a, b):
        if a[1] < b[1]:
            return -1
        elif a[1] > b[1]:
            return 1
        else:
            return 0

    return sorted(tuples_list, key=cmp_to_key(compare))

# Example
tuples = [(1, 2), (3, 1), (5, 0)]
result = sort_by_second_custom(tuples)
print(result)  # [(5, 0), (3, 1), (1, 2)]
