def find_first_index_index(tup, element):
    """Find first occurrence using tuple's built-in index method"""
    try:
        return tup.index(element)
    except ValueError:
        return -1  # Element not found

# Example
my_tuple = (10, 20, 30, 20, 40, 50, 20)
result = find_first_index_index(my_tuple, 20)
print(f"First occurrence of 20 at index: {result}")  # 1
