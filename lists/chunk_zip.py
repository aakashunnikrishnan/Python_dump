def chunk_zip(lst, n):
    """Split list into chunks using zip (only works for exact multiples)"""
    return list(zip(*[iter(lst)] * n))

# For handling remainder
def chunk_zip_remainder(lst, n):
    """Split list into chunks using zip with remainder handling"""
    chunks = [list(chunk) for chunk in zip(*[iter(lst)] * n)]
    remainder = len(lst) % n
    if remainder:
        chunks.append(lst[-remainder:])
    return chunks

# Example
numbers = [1, 2, 3, 4, 5, 6, 7]
result = chunk_zip_remainder(numbers, 3)
print(result)  # [[1, 2, 3], [4, 5, 6], [7]]
