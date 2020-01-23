def rotate_left_inplace(lst, k):
    """Rotate left in-place using reversal algorithm (O(1) extra space)"""
    if not lst:
        return lst

    n = len(lst)
    k = k % n

    # Helper function to reverse a portion of the list
    def reverse(start, end):
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1

    # Step 1: Reverse first k elements
    reverse(0, k - 1)
    # Step 2: Reverse remaining n-k elements
    reverse(k, n - 1)
    # Step 3: Reverse entire list
    reverse(0, n - 1)

    return lst

# Example
original = [1, 2, 3, 4, 5]
result = rotate_left_inplace(original, 2)
print(result)  # [3, 4, 5, 1, 2]
