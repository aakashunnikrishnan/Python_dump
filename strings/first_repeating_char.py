def first_repeating_char(s):
    """Find the first repeating character"""
    seen_chars = set()

    for char in s:
        if char in seen_chars:
            return char
        seen_chars.add(char)

    return None  # Return None if no repeating character found
