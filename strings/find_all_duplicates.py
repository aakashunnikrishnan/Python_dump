def find_all_duplicates(s):
    """Return all duplicate characters with their counts"""
    freq = char_frequency(s)
    duplicates = {}

    for char, count in freq.items():
        if count > 1:
            duplicates[char] = count

    return duplicates
