def remove_duplicates_loop(lst):
    """Traditional approach with a set to track seen items"""
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# Example
original = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
result = remove_duplicates_loop(original)
print(result)  # [1, 2, 3, 4, 5, 6]
