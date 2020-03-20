from collections import Counter

def count_occurrences_counter(tup, element):
    """Count using Counter (useful for multiple elements)"""
    return Counter(tup).get(element, 0)

# Example
my_tuple = (1, 2, 3, 2, 4, 2, 5, 2, 6)
result = count_occurrences_counter(my_tuple, 2)
print(f"Count of 2: {result}")  # 4
