def sort_by_second_descending(tuples_list):
    """Sort by second element in descending order"""
    return sorted(tuples_list, key=lambda x: x[1], reverse=True)

# Example
tuples = [(1, 2), (3, 1), (5, 0)]
result = sort_by_second_descending(tuples)
print(result)  # [(1, 2), (3, 1), (5, 0)]
