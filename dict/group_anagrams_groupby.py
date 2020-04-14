from itertools import groupby

def group_anagrams_groupby(words):
    """Group anagrams using itertools.groupby (requires sorting by key first)"""
    # Sort words by their sorted representation
    words_sorted = sorted(words, key=lambda x: ''.join(sorted(x)))

    # Group by sorted representation
    result = []
    for key, group in groupby(words_sorted, key=lambda x: ''.join(sorted(x))):
        result.append(list(group))

    return result

# Example
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams_groupby(words)
print(result)  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
