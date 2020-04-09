def key_and_value_with_max(dictionary):
    """Return both key and value with maximum value"""
    if not dictionary:
        return None, None

    max_key = max(dictionary, key=dictionary.get)
    return max_key, dictionary[max_key]

# Example
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}
key, value = key_and_value_with_max(scores)
print(f"Key: {key}, Value: {value}")  # Diana, 95
