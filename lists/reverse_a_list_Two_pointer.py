def reverse_list_inplace(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        # Swap elements
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

    return lst

# Example
original = [1, 2, 3, 4]
reverse_list_inplace(original)
print(original)  # [4, 3, 2, 1]
