from collections import deque

def rotate_left_deque(lst, k):
    """Rotate left using deque (efficient for large rotations)"""
    if not lst:
        return lst

    dq = deque(lst)
    dq.rotate(-k)  # Negative for left rotation
    return list(dq)

# Example
original = [1, 2, 3, 4, 5]
result = rotate_left_deque(original, 2)
print(result)  # [3, 4, 5, 1, 2]
