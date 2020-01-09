def trim_spaces_compact(s):
    """More compact version of trim spaces"""
    # Find start index
    start = 0
    while start < string_length(s) and s[start] == ' ':
        start += 1

    # Find end index
    end = string_length(s) - 1
    while end >= start and s[end] == ' ':
        end -= 1

    # Build result
    if start > end:
        return ""

    return s[start:end + 1]  # Using slicing for compactness
