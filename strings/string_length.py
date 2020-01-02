def string_length(s):
    """Find the length of a string without using len()"""
    count = 0
    for _ in s:
        count += 1
    return count
