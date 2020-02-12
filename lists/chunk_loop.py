def chunk_loop(lst, n):
    """Split list into chunks using a for loop"""
    chunks = []
    for i in range(0, len(lst), n):
        chunks.append(lst[i:i + n])
    return chunks

# Example
numbers = [1, 2, 3, 4, 5, 6, 7]
result = chunk_loop(numbers, 3)
print(result)  # [[1, 2, 3], [4, 5, 6], [7]]
