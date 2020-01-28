def find_pairs_with_duplicates(lst, target):
    """Find all pairs including duplicate combinations"""
    from collections import Counter

    freq = Counter(lst)
    pairs = []
    used = set()

    for num in list(freq.keys()):
        complement = target - num

        if complement in freq:
            if num == complement:
                # Handle same number case (e.g., target=8, num=4, complement=4)
                count = freq[num] * (freq[num] - 1) // 2
                for _ in range(count):
                    pairs.append((num, complement))
            elif num < complement and (num, complement) not in used:
                count = freq[num] * freq[complement]
                for _ in range(count):
                    pairs.append((num, complement))
                used.add((num, complement))

    return pairs

# Example with duplicates
numbers = [1, 2, 3, 4, 4, 5, 6, 7, 7]
target = 8
result = find_pairs_with_duplicates(numbers, target)
print(result)  # [(1, 7), (1, 7), (2, 6), (3, 5), (4, 4)]
