def second_largest_sort(lst):
    """Simple approach using sort"""
    if len(lst) < 2:
        return None

    # Sort in descending order
    sorted_lst = sorted(lst, reverse=True)

    # Find first element that's different from largest
    largest = sorted_lst[0]
    for num in sorted_lst:
        if num != largest:
            return num

    return None  # All elements are the same

# Example
numbers = [10, 20, 4, 45, 99]
result = second_largest_sort(numbers)
print(result)  # 45
