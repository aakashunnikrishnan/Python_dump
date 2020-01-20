def reverse_list_comprehension(lst):
    return [lst[i] for i in range(len(lst) - 1, -1, -1)]

# Example
original = [1, 2, 3, 4]
reversed_list = reverse_list_comprehension(original)
print(reversed_list)  # [4, 3, 2, 1]
