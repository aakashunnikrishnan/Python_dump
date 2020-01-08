def sort_string(s):
    """Simple bubble sort for strings"""
    chars = list(s)
    n = string_length(s)

    for i in range(n):
        for j in range(0, n - i - 1):
            if chars[j] > chars[j + 1]:
                chars[j], chars[j + 1] = chars[j + 1], chars[j]

    return ''.join(chars)
