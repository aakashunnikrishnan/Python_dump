from itertools import islice

def chunk_islice(lst, n):
    """Split list into chunks using itertools.islice"""
    it = iter(lst)
    chunks = []

    while True:
        chunk = list(islice(it, n))
        if not chunk:
            break
        chunks.append(chunk)

    return chunks

# Example
numbers = [1, 2, 3, 4, 5, 6, 7]
result = chunk_islice(numbers, 3)
print(result)  # [[1, 2, 3], [4, 5, 6], [7]]
