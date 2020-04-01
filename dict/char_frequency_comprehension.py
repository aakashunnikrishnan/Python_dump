def char_frequency_comprehension(s):
    """Count character frequency using dictionary comprehension"""
    return {char: s.count(char) for char in set(s)}

# Example
text = "hello world"
result = char_frequency_comprehension(text)
print(result)
