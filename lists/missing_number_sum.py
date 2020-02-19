def missing_number_sum(lst, n=None):
    """Find missing number using sum formula: n(n+1)/2"""
    if not lst:
        return 1 if n == 1 else None

    # If n not provided, calculate from list length + 1
    if n is None:
        n = len(lst) + 1

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)

    return expected_sum - actual_sum

# Example
numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]  # Missing 7
result = missing_number_sum(numbers)
print(result)  # 7
