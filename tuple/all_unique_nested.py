def all_unique_nested(tup):
    """Check uniqueness using nested loops"""
    for i in range(len(tup)):
        for j in range(i + 1, len(tup)):
            if tup[i] == tup[j]:
                return False
    return True

# Example
tup1 = (1, 2, 3, 4, 5)
tup2 = (1, 2, 3, 2, 4, 5)
print(all_unique_nested(tup1))  # True
print(all_unique_nested(tup2))  # False
