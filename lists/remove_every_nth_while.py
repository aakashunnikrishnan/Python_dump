def remove_every_nth_while(lst, n):
    """Remove every nth element using while loop"""
    if n <= 0:
        return lst

    result = []
    i = 1
    for item in lst:
        if i % n != 0:
            result.append(item)
        i += 1

    return result

# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_every_nth_while(numbers, 3)
print(result)  # [1, 2, 4, 5, 7, 8, 10]
