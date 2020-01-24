def is_palindrome_recursive(lst):
    """Check palindrome recursively"""
    if len(lst) <= 1:
        return True

    if lst[0] != lst[-1]:
        return False

    return is_palindrome_recursive(lst[1:-1])

# Example
print(is_palindrome_recursive([1, 2, 3, 2, 1]))  # True
print(is_palindrome_recursive([1, 2, 3, 4, 5]))  # False
