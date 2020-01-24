def is_palindrome_reversed(lst):
    """Check palindrome using reversed() function"""
    return lst == list(reversed(lst))

# Example
print(is_palindrome_reversed([1, 2, 3, 2, 1]))  # True
print(is_palindrome_reversed([1, 2, 3, 4, 5]))  # False
