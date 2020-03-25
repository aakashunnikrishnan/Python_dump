from collections import Counter

def all_unique_counter(tup):
    """Check uniqueness using Counter"""
    counts = Counter(tup)
    return all(count == 1 for count in counts.values())

# Example
tup1 = (1, 2, 3, 4, 5)
tup2 = (1, 2, 3, 2, 4, 5)
print(all_unique_counter(tup1))  # True
print(all_unique_counter(tup2))  # False
