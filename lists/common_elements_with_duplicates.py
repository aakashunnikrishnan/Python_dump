from collections import Counter

def common_elements_with_duplicates(list1, list2):
    """Find common elements including duplicates (multiset intersection)"""
    counter1 = Counter(list1)
    counter2 = Counter(list2)

    result = []
    for item in counter1:
        if item in counter2:
            result.extend([item] * min(counter1[item], counter2[item]))

    return result

# Example with duplicates
list1 = [1, 2, 2, 3, 4, 4, 4, 5]
list2 = [2, 2, 4, 4, 6, 7]
result = common_elements_with_duplicates(list1, list2)
print(result)  # [2, 2, 4, 4]
