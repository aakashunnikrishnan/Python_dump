from collections import OrderedDict

def remove_duplicates_ordereddict(lst):
    """Uses OrderedDict for older Python versions"""
    return list(OrderedDict.fromkeys(lst))

# Example
original = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
result = remove_duplicates_ordereddict(original)
print(result)  # [1, 2, 3, 4, 5, 6]
