def second_largest_set(lst):
    """Handles duplicates by converting to set"""
    if len(lst) < 2:
        return None

    # Remove duplicates and sort in descending order
    unique_sorted = sorted(set(lst), reverse=True)

    if len(unique_sorted) >= 2:
        return unique_sorted[1]
    return None

# Example
numbers = [10, 20, 4, 45, 99, 99, 99]
result = second_largest_set(numbers)
print(result)  # 45
