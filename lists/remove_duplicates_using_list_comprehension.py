def remove_duplicates_comprehension(lst):
    """List comprehension with a set for tracking"""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# Example
original = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
result = remove_duplicates_comprehension(original)
print(result)  # [1, 2, 3, 4, 5, 6]
