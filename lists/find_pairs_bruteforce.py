def find_pairs_bruteforce(lst, target):
    """Find all pairs using nested loops"""
    pairs = []
    n = len(lst)

    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))

    return pairs

# Example
numbers = [1, 2, 3, 4, 5, 6, 7]
target = 8
result = find_pairs_bruteforce(numbers, target)
print(result)  # [(1, 7), (2, 6), (3, 5)]
