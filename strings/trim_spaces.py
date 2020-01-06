def trim_spaces(s):
    """Remove leading and trailing spaces without using strip()"""
    # Find first non-space character
    start = 0
    while start < string_length(s) and s[start] == ' ':
        start += 1

    # Find last non-space character
    end = string_length(s) - 1
    while end >= 0 and s[end] == ' ':
        end -= 1

    # Extract the trimmed string
    if start > end:  # String is all spaces
        return ""

    result = ""
    for i in range(start, end + 1):
        result += s[i]
    return result
