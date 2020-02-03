def flatten_recursive(nested_list):
    """Flatten nested list using recursion"""
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_recursive(item))
        else:
            result.append(item)

    return result

# Example
nested = [1, [2, [3, 4]], 5]
result = flatten_recursive(nested)
print(result)  # [1, 2, 3, 4, 5]
