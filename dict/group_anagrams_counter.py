from collections import Counter, defaultdict

def group_anagrams_counter(words):
    """Group anagrams using Counter (frequency dictionary) as key"""
    anagrams = defaultdict(list)

    for word in words:
        # Use frozenset of Counter items as key (hashable)
        counter = Counter(word)
        key = frozenset(counter.items())  # Immutable representation
        anagrams[key].append(word)

    return list(anagrams.values())

# Example
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams_counter(words)
print(result)  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
