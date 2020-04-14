def group_anagrams_manual(words):
    """Group anagrams using manual dictionary (no defaultdict)"""
    anagrams = {}

    for word in words:
        key = ''.join(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]

    return list(anagrams.values())

# Example
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams_manual(words)
print(result)  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
