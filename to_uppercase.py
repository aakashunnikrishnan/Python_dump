def to_uppercase(s):
    """Convert a string to uppercase without using upper()"""
    result = ""
    for char in s:
        if 97 <= ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    return result
