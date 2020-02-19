def missing_number_xor(lst, n=None):
    """Find missing number using XOR (no overflow issues)"""
    if n is None:
        n = len(lst) + 1

    # XOR all numbers from 1 to n
    xor_full = 0
    for i in range(1, n + 1):
        xor_full ^= i

    # XOR all numbers in the list
    xor_list = 0
    for num in lst:
        xor_list ^= num

    # Missing number is XOR of both
    return xor_full ^ xor_list

# Example
numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]
result = missing_number_xor(numbers)
print(result)  # 7
