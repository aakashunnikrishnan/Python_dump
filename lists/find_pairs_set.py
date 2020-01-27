def find_pairs_set(lst, target):
    """Find all pairs using a set for O(n) time complexity"""
    seen = set()
    pairs = []

    for num in lst:
        complement = target - num

        if complement in seen:
            pairs.append((complement, num))

        seen.add(num)

    return pairs

# Example
numbers = [1, 2, 3, 4, 5, 6, 7]
target = 8
result = find_pairs_set(numbers, target)
print(result)  # [(1, 7), (2, 6), (3, 5)]
