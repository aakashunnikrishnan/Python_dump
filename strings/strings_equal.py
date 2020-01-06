def strings_equal(s1, s2):
    """Check if two strings are equal without using == operator"""
    # First check lengths
    if string_length(s1) != string_length(s2):
        return False

    # Compare character by character
    for i in range(string_length(s1)):
        if s1[i] != s2[i]:
            return False
    return True
