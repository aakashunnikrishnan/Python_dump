def least_frequent_char(s):
    """Find the least frequent character in a string"""
    if not s:
        return None

    freq = char_frequency(s)
    least_freq = None
    min_count = float('inf')

    for char, count in freq.items():
        if count < min_count:
            min_count = count
            least_freq = char

    return least_freq, min_count
