def most_frequent_chars(s):
    """Find all characters with maximum frequency (if multiple)"""
    if not s:
        return []

    freq = char_frequency(s)
    max_count = 0
    max_chars = []

    # Find maximum count
    for count in freq.values():
        if count > max_count:
            max_count = count

    # Find all characters with max_count
    for char, count in freq.items():
        if count == max_count:
            max_chars.append(char)

    return max_chars, max_count
