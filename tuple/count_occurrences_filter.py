def count_occurrences_filter(tup, element):
    """Count using filter() function"""
    return len(list(filter(lambda x: x == element, tup)))

# Example
my_tuple = (1, 2, 3, 2, 4, 2, 5, 2, 6)
result = count_occurrences_filter(my_tuple, 2)
print(f"Count of 2: {result}")  # 4
