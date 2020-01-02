def reverse_string(s):
    """Reverse a given string"""
    result = ""
    for char in s:
        result = char + result
    return result

def is_palindrome(s):
    """Check if a string is a palindrome"""
    reversed_str = reverse_string(s)
    return s == reversed_str
