def least_frequent_chars(s):
    """Find all characters with minimum frequency (if multiple)"""
    if not s:
        return []

    freq = char_frequency(s)
    min_count = float('inf')
    min_chars = []

    # Find minimum count
    for count in freq.values():
        if count < min_count:
            min_count = count

    # Find all characters with min_count
    for char, count in freq.items():
        if count == min_count:
            min_chars.append(char)

    return min_chars, min_count
