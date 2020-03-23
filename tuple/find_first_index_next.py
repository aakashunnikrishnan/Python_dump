def find_first_index_next(tup, element):
    """Find first occurrence using next() with generator"""
    try:
        return next(i for i, item in enumerate(tup) if item == element)
    except StopIteration:
        return -1

# Example
my_tuple = (10, 20, 30, 20, 40, 50, 20)
result = find_first_index_next(my_tuple, 20)
print(f"First occurrence of 20 at index: {result}")  # 1
