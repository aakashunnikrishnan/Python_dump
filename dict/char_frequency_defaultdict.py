from collections import defaultdict

def char_frequency_defaultdict(s):
    """Count character frequency using defaultdict"""
    freq = defaultdict(int)

    for char in s:
        freq[char] += 1

    return dict(freq)

# Example
text = "hello world"
result = char_frequency_defaultdict(text)
print(result)
