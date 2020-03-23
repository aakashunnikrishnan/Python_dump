def find_first_index_list(tup, element):
    """Convert to list and use index (less efficient)"""
    try:
        return list(tup).index(element)
    except ValueError:
        return -1

# Example
my_tuple = (10, 20, 30, 20, 40, 50, 20)
result = find_first_index_list(my_tuple, 20)
print(f"First occurrence of 20 at index: {result}")  # 1
