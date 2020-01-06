def are_anagrams(s1, s2):
    """Check if two strings are anagrams"""
    # Remove spaces and convert to lowercase for comparison
    s1_clean = remove_spaces(to_lowercase(s1))
    s2_clean = remove_spaces(to_lowercase(s2))

    # If lengths are different, they can't be anagrams
    if string_length(s1_clean) != string_length(s2_clean):
        return False

    # Count occurrences of each character in both strings
    char_count = {}

    # Count characters in first string
    for char in s1_clean:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Subtract counts for second string
    for char in s2_clean:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    # Check all counts are zero
    for count in char_count.values():
        if count != 0:
            return False

    return True
