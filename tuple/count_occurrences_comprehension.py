def count_occurrences_comprehension(tup, element):
    """Count using list comprehension and sum()"""
    return sum(1 for item in tup if item == element)

# Example
my_tuple = (1, 2, 3, 2, 4, 2, 5, 2, 6)
result = count_occurrences_comprehension(my_tuple, 2)
print(f"Count of 2: {result}")  # 4
