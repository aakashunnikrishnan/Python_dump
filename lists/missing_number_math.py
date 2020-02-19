def missing_number_math(lst):
    """Find missing number using sum (handles case when first or last missing)"""
    if not lst:
        return 1

    n = len(lst) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)

    if expected_sum == actual_sum:
        # All numbers present? Actually one should be missing
        return None

    return expected_sum - actual_sum

# Example
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]  # Missing 1
result = missing_number_math(numbers)
print(result)  # 1
