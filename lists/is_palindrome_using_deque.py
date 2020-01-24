from collections import deque

def is_palindrome_deque(lst):
    """Check palindrome using deque (pops from both ends)"""
    dq = deque(lst)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

    return True

# Example
print(is_palindrome_deque([1, 2, 3, 2, 1]))  # True
print(is_palindrome_deque([1, 2, 3, 4, 5]))  # False
