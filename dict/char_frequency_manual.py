def char_frequency_manual(s):
    """Count character frequency using manual dictionary"""
    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

# Example
text = "hello world"
result = char_frequency_manual(text)
print(result)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
