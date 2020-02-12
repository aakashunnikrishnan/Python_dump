def chunk_generator(lst, n):
    """Split list into chunks using a generator (memory efficient)"""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Example
numbers = [1, 2, 3, 4, 5, 6, 7]
result = list(chunk_generator(numbers, 3))
print(result)  # [[1, 2, 3], [4, 5, 6], [7]]
