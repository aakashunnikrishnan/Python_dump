def count_occurrences_case_insensitive(s, target_char):
    """Count occurrences ignoring case"""
    s_lower = to_lowercase(s)
    target_lower = to_lowercase(target_char)
    count = 0
    for char in s_lower:
        if char == target_lower:
            count += 1
    return count
