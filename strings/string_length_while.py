def string_length_while(s):
    """Find length using while loop"""
    count = 0
    try:
        while True:
            # Try to access each character until IndexError
            _ = s[count]
            count += 1
    except IndexError:
        pass
    return count
