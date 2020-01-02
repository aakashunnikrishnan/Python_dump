def reverse_string(s):
    """Reverse a given string"""
    result = ""
    for char in s:
        result = char + result
    return result
