import heapq

def merge_heapq(list1, list2):
    """Merge using heapq.merge (returns iterator)"""
    return list(heapq.merge(list1, list2))

# Example
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = merge_heapq(list1, list2)
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8]
