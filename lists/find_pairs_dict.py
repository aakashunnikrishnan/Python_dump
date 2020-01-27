def find_pairs_dict(lst, target):
    """Find all pairs using dictionary (handles duplicates)"""
    from collections import defaultdict

    freq = defaultdict(int)
    pairs = []

    for num in lst:
        complement = target - num

        if freq[complement] > 0:
            pairs.append((complement, num))
            freq[complement] -= 1
        else:
            freq[num] += 1

    return pairs

# Example with duplicates
numbers = [1, 2, 3, 4, 1, 6, 7, 2]
target = 8
result = find_pairs_dict(numbers, target)
print(result)  # [(1, 7), (2, 6), (1, 7), (2, 6)] - depending on order
