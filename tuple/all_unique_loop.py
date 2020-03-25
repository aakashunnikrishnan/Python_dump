def all_unique_loop(tup):
    """Check uniqueness using loop with early exit"""
    seen = set()
    for item in tup:
        if item in seen:
            return False
        seen.add(item)
    return True

# Example
tup1 = (1, 2, 3, 4, 5)
tup2 = (1, 2, 3, 2, 4, 5)
print(all_unique_loop(tup1))  # True
print(all_unique_loop(tup2))  # False
