def second_largest_single_pass(lst):
    """Find second largest in one pass without sorting"""
    if len(lst) < 2:
        return None

    largest = second = float('-inf')

    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second if second != float('-inf') else None

# Example
numbers = [10, 20, 4, 45, 99, 99, 99]
result = second_largest_single_pass(numbers)
print(result)  # 45
