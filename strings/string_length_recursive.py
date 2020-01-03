def string_length_recursive(s):
    """Find length using recursion"""
    if s == "":
        return 0
    return 1 + string_length_recursive(s[1:])
