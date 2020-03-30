def char_frequency_get(s):
    """Count character frequency using dict.get()"""
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    return freq

# Example
text = "hello world"
result = char_frequency_get(text)
print(result)
