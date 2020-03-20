def count_occurrences_count(tup, element):
    """Count occurrences using tuple's built-in count method"""
    return tup.count(element)

# Example
my_tuple = (1, 2, 3, 2, 4, 2, 5, 2, 6)
result = count_occurrences_count(my_tuple, 2)
print(f"Count of 2: {result}")  # 4
