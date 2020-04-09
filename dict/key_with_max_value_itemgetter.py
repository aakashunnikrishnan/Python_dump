from operator import itemgetter

def key_with_max_value_itemgetter(dictionary):
    """Find key with maximum value using itemgetter"""
    if not dictionary:
        return None

    return max(dictionary.items(), key=itemgetter(1))[0]

# Example
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}
result = key_with_max_value_itemgetter(scores)
print(f"Key with max value: {result}")  # Diana
