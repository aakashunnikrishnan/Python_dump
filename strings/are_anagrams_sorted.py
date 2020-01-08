def are_anagrams_sorted(s1, s2):
    """Alternative: Check anagrams by sorting"""
    s1_clean = remove_spaces(to_lowercase(s1))
    s2_clean = remove_spaces(to_lowercase(s2))

    # Sort characters (simulate sorting without sort())
    s1_sorted = sort_string(s1_clean)
    s2_sorted = sort_string(s2_clean)

    return strings_equal(s1_sorted, s2_sorted)
