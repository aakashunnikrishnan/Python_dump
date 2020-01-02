def remove_spaces(s):
    """Remove spaces from a string"""
    result = ""
    for char in s:
        if char != ' ':
            result += char
    return result
