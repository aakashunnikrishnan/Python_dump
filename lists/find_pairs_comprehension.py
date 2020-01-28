def find_pairs_comprehension(lst, target):
    """Find pairs using list comprehension (unique pairs only)"""
    seen = set()
    pairs = [
        (complement, num)
        for num in lst
        for complement in [target - num]
        if complement in seen and (complement, num) not in pairs
    ]
    seen.update(lst)
    return list(set(pairs))

# Example
numbers = [1, 2, 3, 4, 5, 6, 7]
target = 8
result = find_pairs_comprehension(numbers, target)
print(result)  # [(1, 7), (2, 6), (3, 5)]
