def remove_duplicates_dict(lst):
    """Uses dict to maintain order (Python 3.7+ guaranteed)"""
    return list(dict.fromkeys(lst))

# Example
original = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
result = remove_duplicates_dict(original)
print(result)  # [1, 2, 3, 4, 5, 6]
