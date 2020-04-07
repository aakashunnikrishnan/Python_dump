def key_with_max_value_max(dictionary):
    """Find key with maximum value using max() with key parameter"""
    if not dictionary:
        return None

    return max(dictionary, key=dictionary.get)

# Example
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}
result = key_with_max_value_max(scores)
print(f"Key with max value: {result}")  # Diana
