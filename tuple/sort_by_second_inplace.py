def sort_by_second_inplace(tuples_list):
    """Sort list of tuples by second element in-place"""
    tuples_list.sort(key=lambda x: x[1])
    return tuples_list

# Example
tuples = [(1, 2), (3, 1), (5, 0)]
result = sort_by_second_inplace(tuples)
print(result)  # [(5, 0), (3, 1), (1, 2)]
