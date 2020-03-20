from functools import reduce

def count_occurrences_reduce(tup, element):
    """Count using reduce function"""
    return reduce(lambda count, x: count + (1 if x == element else 0), tup, 0)

# Example
my_tuple = (1, 2, 3, 2, 4, 2, 5, 2, 6)
result = count_occurrences_reduce(my_tuple, 2)
print(f"Count of 2: {result}")  # 4
