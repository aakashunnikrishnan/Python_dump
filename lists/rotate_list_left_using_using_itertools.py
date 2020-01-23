from itertools import islice, chain

def rotate_left_itertools(lst, k):
    """Rotate left using itertools"""
    if not lst:
        return lst

    n = len(lst)
    k = k % n

    # Create iterator and slice
    it = iter(lst)
    return list(chain(islice(it, k, None), islice(lst, k)))

# Example
original = [1, 2, 3, 4, 5]
result = rotate_left_itertools(original, 2)
print(result)  # [3, 4, 5, 1, 2]
