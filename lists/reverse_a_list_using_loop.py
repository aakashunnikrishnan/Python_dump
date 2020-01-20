def reverse_list_loop(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# Example
original = [1, 2, 3, 4]
reversed_list = reverse_list_loop(original)
print(reversed_list)  # [4, 3, 2, 1]
