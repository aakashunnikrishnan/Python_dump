def reverse_list_recursive(lst):
    if len(lst) <= 1:
        return lst
    return reverse_list_recursive(lst[1:]) + [lst[0]]

# Example
original = [1, 2, 3, 4]
reversed_list = reverse_list_recursive(original)
print(reversed_list)  # [4, 3, 2, 1]
