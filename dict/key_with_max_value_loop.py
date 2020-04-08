def key_with_max_value_loop(dictionary):
    """Find key with maximum value using manual loop"""
    if not dictionary:
        return None

    max_key = None
    max_value = float('-inf')

    for key, value in dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key

# Example
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}
result = key_with_max_value_loop(scores)
print(f"Key with max value: {result}")  # Diana
