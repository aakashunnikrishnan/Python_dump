def spaces_to_underscores_list(s):
    """Replace spaces with underscores using list comprehension"""
    return ''.join(['_' if char == ' ' else char for char in s])
