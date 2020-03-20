def count_occurrences_loop(tup, element):
    """Count occurrences using a for loop"""
    count = 0
    for item in tup:
        if item == element:
            count += 1
    return count

# Example
my_tuple = (1, 2, 3, 2, 4, 2, 5, 2, 6)
result = count_occurrences_loop(my_tuple, 2)
print(f"Count of 2: {result}")  # 4
