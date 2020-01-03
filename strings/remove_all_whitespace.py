def remove_all_whitespace(s):
    """Remove all whitespace characters (spaces, tabs, newlines)"""
    result = ""
    for char in s:
        if char not in ' \t\n\r':
            result += char
    return result
