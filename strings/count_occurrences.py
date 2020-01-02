def count_occurrences(s, target_char):
    """Count occurrences of a given character"""
    count = 0
    for char in s:
        if char == target_char:
            count += 1
    return count
