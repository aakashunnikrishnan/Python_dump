def char_frequency_setdefault(s):
    """Count character frequency using dict.setdefault()"""
    freq = {}

    for char in s:
        freq.setdefault(char, 0)
        freq[char] += 1

    return freq

# Example
text = "hello world"
result = char_frequency_setdefault(text)
print(result)
