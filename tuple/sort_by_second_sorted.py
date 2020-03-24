def sort_by_second_sorted(tuples_list):
    """Sort list of tuples by second element using sorted()"""
    return sorted(tuples_list, key=lambda x: x[1])

# Example
tuples = [(1, 2), (3, 1), (5, 0)]
result = sort_by_second_sorted(tuples)
print(result)  # [(5, 0), (3, 1), (1, 2)]
