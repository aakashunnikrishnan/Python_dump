def remove_duplicates(s):
    """Remove duplicate characters while preserving order"""
    seen = set()
    result = ""

    for char in s:
        if char not in seen:
            seen.add(char)
            result += char

    return result
