def to_lowercase(s):
    """Convert a string to lowercase without using lower()"""
    result = ""
    for char in s:
        # Check if character is uppercase (ASCII: 65-90)
        if 65 <= ord(char) <= 90:
            # Convert to lowercase by adding 32
            result += chr(ord(char) + 32)
        else:
            result += char
    return result
