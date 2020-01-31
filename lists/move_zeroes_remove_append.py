def move_zeroes_remove_append(lst):
    """Remove zeroes and append them (modifies original)"""
    i = 0
    n = len(lst)
    while i < len(lst):
        if lst[i] == 0:
            lst.pop(i)
            lst.append(0)
        else:
            i += 1
    return lst

# Example
numbers = [0, 1, 0, 3, 0, 12, 0, 5]
result = move_zeroes_remove_append(numbers.copy())
print(result)  # [1, 3, 12, 5, 0, 0, 0, 0]
