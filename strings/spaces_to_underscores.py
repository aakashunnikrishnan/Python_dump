def spaces_to_underscores(s):
    """Replace all spaces with underscores"""
    result = ""
    for char in s:
        if char == ' ':
            result += '_'
        else:
            result += char
    return result
