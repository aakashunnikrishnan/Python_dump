def char_frequency(s):
    """Count frequency of each character in a string"""
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
