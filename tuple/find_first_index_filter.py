def find_first_index_filter(tup, element):
    """Find first occurrence using filter()"""
    indices = filter(lambda x: x[1] == element, enumerate(tup))
    try:
        return next(indices)[0]
    except StopIteration:
        return -1

# Example
my_tuple = (10, 20, 30, 20, 40, 50, 20)
result = find_first_index_filter(my_tuple, 20)
print(f"First occurrence of 20 at index: {result}")  # 1
