def missing_number_set(lst, n=None):
    """Find missing number using set difference"""
    if n is None:
        n = len(lst) + 1

    full_set = set(range(1, n + 1))
    list_set = set(lst)

    missing = full_set - list_set
    return missing.pop() if missing else None

# Example
numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]
result = missing_number_set(numbers)
print(result)  # 7
