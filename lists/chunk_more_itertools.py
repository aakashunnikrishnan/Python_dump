# Requires: pip install more-itertools
from more_itertools import chunked

def chunk_more_itertools(lst, n):
    """Split list into chunks using more_itertools"""
    return list(chunked(lst, n))

# Example - uncomment if you have more-itertools installed
# numbers = [1, 2, 3, 4, 5, 6, 7]
# result = chunk_more_itertools(numbers, 3)
# print(result)  # [[1, 2, 3], [4, 5, 6], [7]]
