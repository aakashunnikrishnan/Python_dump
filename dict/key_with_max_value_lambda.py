def key_with_max_value_lambda(dictionary):
    """Find key with maximum value using lambda"""
    if not dictionary:
        return None

    return max(dictionary, key=lambda k: dictionary[k])

# Example
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}
result = key_with_max_value_lambda(scores)
print(f"Key with max value: {result}")  # Diana
