def is_palindrome_two_pointer(lst):
    """Check palindrome using two pointers (O(1) extra space)"""
    left = 0
    right = len(lst) - 1

    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1

    return True

# Example
print(is_palindrome_two_pointer([1, 2, 3, 2, 1]))  # True
print(is_palindrome_two_pointer([1, 2, 3, 4, 5]))  # False
