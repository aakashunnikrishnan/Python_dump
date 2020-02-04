from functools import reduce

def flatten_reduce(nested_list):
    """Flatten using reduce (works for one level only, recursive version)"""
    def flatten_two_levels(x, y):
        if isinstance(y, list):
            return x + flatten_reduce(y)
        return x + [y]

    return reduce(flatten_two_levels, nested_list, [])

# Example
nested = [1, [2, [3, 4]], 5]
result = flatten_reduce(nested)
print(result)  # [1, 2, 3, 4, 5]
