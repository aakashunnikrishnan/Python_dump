def all_unique_set(tup):
    """Check if all elements are unique using set"""
    return len(tup) == len(set(tup))

# Example
tup1 = (1, 2, 3, 4, 5)
tup2 = (1, 2, 3, 2, 4, 5)
print(all_unique_set(tup1))  # True
print(all_unique_set(tup2))  # False
