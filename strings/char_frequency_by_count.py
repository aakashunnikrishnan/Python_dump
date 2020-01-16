def char_frequency_by_count(s):
    """Character frequency sorted by count (descending)"""
    freq = char_frequency(s)

    # Sort by frequency (descending)
    sorted_items = []
    for char, count in freq.items():
        sorted_items.append((count, char))

    sorted_items.sort(reverse=True)

    # Convert back to character: count format
    result = {}
    for count, char in sorted_items:
        result[char] = count

    return result
