import numpy as np

def flatten_numpy(nested_list):
    """Flatten using numpy (only works for numeric data)"""
    return list(np.array(nested_list, dtype=object).flatten())

# Example
nested = [1, [2, [3, 4]], 5]
result = flatten_numpy(nested)
print(result)  # [1, 2, 3, 4, 5]
