def find_first_index_loop(tup, element):
    """Find first occurrence using a for loop"""
    for i, item in enumerate(tup):
        if item == element:
            return i
    return -1  # Element not found

# Example
my_tuple = (10, 20, 30, 20, 40, 50, 20)
result = find_first_index_loop(my_tuple, 20)
print(f"First occurrence of 20 at index: {result}")  # 1
