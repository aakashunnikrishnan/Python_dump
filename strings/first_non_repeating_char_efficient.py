def first_non_repeating_char_efficient(s):
    """More efficient version using list for order tracking"""
    from collections import OrderedDict

    char_count = OrderedDict()

    # Count characters and maintain insertion order
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find first character with count 1
    for char, count in char_count.items():
        if count == 1:
            return char

    return None
