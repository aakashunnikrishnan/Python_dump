def group_anagrams_sorted(words):
    """Group anagrams using sorted string as dictionary key"""
    from collections import defaultdict

    anagrams = defaultdict(list)

    for word in words:
        # Sort the word to create a key (e.g., "eat" -> "aet")
        key = ''.join(sorted(word))
        anagrams[key].append(word)

    return list(anagrams.values())

# Example
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams_sorted(words)
print(result)  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
