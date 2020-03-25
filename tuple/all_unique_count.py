def all_unique_count(tup):
    """Check uniqueness using list comprehension"""
    return all(tup.count(item) == 1 for item in tup)

# Example
tup1 = (1, 2, 3, 4, 5)
tup2 = (1, 2, 3, 2, 4, 5)
print(all_unique_count(tup1))  # True
print(all_unique_count(tup2))  # False
