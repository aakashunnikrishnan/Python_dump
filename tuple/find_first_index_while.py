def find_first_index_while(tup, element):
    """Find first occurrence using while loop"""
    i = 0
    while i < len(tup):
        if tup[i] == element:
            return i
        i += 1
    return -1

# Example
my_tuple = (10, 20, 30, 20, 40, 50, 20)
result = find_first_index_while(my_tuple, 20)
print(f"First occurrence of 20 at index: {result}")  # 1
