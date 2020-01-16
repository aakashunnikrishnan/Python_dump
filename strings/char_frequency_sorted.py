def char_frequency_sorted(s):
    """Character frequency with sorted output"""
    freq = char_frequency(s)

    # Sort by character
    sorted_items = []
    for char in sorted(freq.keys()):
        sorted_items.append((char, freq[char]))

    return dict(sorted_items)
