def key_with_max_value_sorted(dictionary):
    """Find key with maximum value using sorted()"""
    if not dictionary:
        return None

    return sorted(dictionary, key=dictionary.get, reverse=True)[0]

# Example
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}
result = key_with_max_value_sorted(scores)
print(f"Key with max value: {result}")  # Diana
