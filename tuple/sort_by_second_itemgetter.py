from operator import itemgetter

def sort_by_second_itemgetter(tuples_list):
    """Sort using itemgetter (faster for large lists)"""
    return sorted(tuples_list, key=itemgetter(1))

# Example
tuples = [(1, 2), (3, 1), (5, 0)]
result = sort_by_second_itemgetter(tuples)
print(result)  # [(5, 0), (3, 1), (1, 2)]
