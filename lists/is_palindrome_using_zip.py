def is_palindrome_all(lst):
    """Check palindrome using all() and zip()"""
    n = len(lst)
    return all(lst[i] == lst[n-1-i] for i in range(n // 2))

# Example
print(is_palindrome_all([1, 2, 3, 2, 1]))  # True
print(is_palindrome_all([1, 2, 3, 4, 5]))  # False
