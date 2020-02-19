def missing_number_dict(lst, n=None):
    """Find missing number using dictionary"""
    if n is None:
        n = len(lst) + 1

    num_dict = {i: False for i in range(1, n + 1)}

    for num in lst:
        num_dict[num] = True

    for num, present in num_dict.items():
        if not present:
            return num

    return None

# Example
numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]
result = missing_number_dict(numbers)
print(result)  # 7
