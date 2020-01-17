def find_chars_by_frequency(s, target_freq):
    """Find all characters with a specific frequency"""
    freq = char_frequency(s)
    result = []

    for char, count in freq.items():
        if count == target_freq:
            result.append(char)

    return result
