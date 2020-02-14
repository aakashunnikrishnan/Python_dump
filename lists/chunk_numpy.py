import numpy as np

def chunk_numpy(lst, n):
    """Split list into chunks using numpy (returns list of arrays)"""
    arr = np.array(lst)
    chunks = np.array_split(arr, (len(lst) + n - 1) // n)
    return [chunk.tolist() for chunk in chunks]

# Example
numbers = [1, 2, 3, 4, 5, 6, 7]
result = chunk_numpy(numbers, 3)
print(result)  # [[1, 2, 3], [4, 5, 6], [7]]
