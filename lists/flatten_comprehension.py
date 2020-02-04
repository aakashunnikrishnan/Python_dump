def flatten_comprehension(nested_list):
    """Flatten using nested list comprehension with recursion"""
    return [item for sublist in nested_list
            for item in (flatten_comprehension(sublist) if isinstance(sublist, list) else [sublist])]

# Example
nested = [1, [2, [3, 4]], 5]
result = flatten_comprehension(nested)
print(result)  # [1, 2, 3, 4, 5]
