def is_palindrome_slice(lst):
    """Check palindrome by comparing with reversed slice"""
    return lst == lst[::-1]

# Example
print(is_palindrome_slice([1, 2, 3, 2, 1]))  # True
print(is_palindrome_slice([1, 2, 3, 4, 5]))  # False
print(is_palindrome_slice(['a', 'b', 'b', 'a']))  # True
