def missing_number_sort(lst):
    """Find missing number by sorting and comparing"""
    if not lst:
        return 1

    lst_sorted = sorted(lst)

    # Check for missing in between
    for i in range(len(lst_sorted)):
        if lst_sorted[i] != i + 1:
            return i + 1

    # If all numbers present, missing is last number
    return len(lst_sorted) + 1

# Example
numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]
result = missing_number_sort(numbers)
print(result)  # 7
