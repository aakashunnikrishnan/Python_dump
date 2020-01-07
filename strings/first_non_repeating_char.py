def first_non_repeating_char(s):
    """Find the first non-repeating character"""
    char_count = {}

    # First pass: count all characters
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Second pass: find first character with count 1
    for char in s:
        if char_count[char] == 1:
            return char

    return None  # Return None if no non-repeating character found
