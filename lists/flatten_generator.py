def flatten_generator(nested_list):
    """Flatten nested list using generator (yield)"""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_generator(item)
        else:
            yield item

# Example
nested = [1, [2, [3, 4]], 5]
result = list(flatten_generator(nested))
print(result)  # [1, 2, 3, 4, 5]
