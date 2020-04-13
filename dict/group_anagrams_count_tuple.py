def group_anagrams_count_tuple(words):
    """Group anagrams using tuple of character counts as key"""
    from collections import defaultdict

    anagrams = defaultdict(list)

    for word in words:
        # Create a tuple of 26 counts for 'a' to 'z'
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        anagrams[tuple(count)].append(word)

    return list(anagrams.values())

# Example
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams_count_tuple(words)
print(result)  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
