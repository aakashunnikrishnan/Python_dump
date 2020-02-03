def flatten_stack(nested_list):
    """Flatten nested list using an explicit stack"""
    result = []
    stack = list(reversed(nested_list))

    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(reversed(item))
        else:
            result.append(item)

    return result

# Example
nested = [1, [2, [3, 4]], 5]
result = flatten_stack(nested)
print(result)  # [1, 2, 3, 4, 5]
