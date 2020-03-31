from collections import Counter

def char_frequency_counter(s):
    """Count character frequency using Counter"""
    return dict(Counter(s))

# Example
text = "hello world"
result = char_frequency_counter(text)
print(result)
