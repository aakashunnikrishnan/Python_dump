def remove_duplicates_with_count(s, max_allowed=1):
    """
    Remove characters that appear more than max_allowed times
    while preserving order
    """
    freq = char_frequency(s)
    result = ""

    for char in s:
        if freq[char] <= max_allowed:
            result += char

    return result
