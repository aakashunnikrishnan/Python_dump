def all_unique_sorted(tup):
    """Check uniqueness by sorting and comparing adjacent elements"""
    if len(tup) <= 1:
        return True

    sorted_tup = sorted(tup)
    for i in range(len(sorted_tup) - 1):
        if sorted_tup[i] == sorted_tup[i + 1]:
            return False
    return True

# Example
tup1 = (1, 2, 3, 4, 5)
tup2 = (1, 2, 3, 2, 4, 5)
print(all_unique_sorted(tup1))  # True
print(all_unique_sorted(tup2))  # False
