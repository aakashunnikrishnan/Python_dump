def most_frequent_char(s):
    """Find the most frequent character in a string"""
    if not s:
        return None

    freq = char_frequency(s)
    most_freq = None
    max_count = 0

    for char, count in freq.items():
        if count > max_count:
            max_count = count
            most_freq = char

    return most_freq, max_count
