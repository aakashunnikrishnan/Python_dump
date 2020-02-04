# Requires: pip install more-itertools
from more_itertools import collapse

def flatten_more_itertools(nested_list):
    """Flatten using more_itertools library"""
    return list(collapse(nested_list))

# Example - uncomment if you have more-itertools installed
# nested = [1, [2, [3, 4]], 5]
# result = flatten_more_itertools(nested)
# print(result)  # [1, 2, 3, 4, 5]
