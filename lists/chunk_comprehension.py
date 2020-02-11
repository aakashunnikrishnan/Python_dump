def chunk_comprehension(lst, n):
    """Split list into chunks using list comprehension"""
    return [lst[i:i + n] for i in range(0, len(lst), n)]

# Example
numbers = [1, 2, 3, 4, 5, 6, 7]
result = chunk_comprehension(numbers, 3)
print(result)  # [[1, 2, 3], [4, 5, 6], [7]]
