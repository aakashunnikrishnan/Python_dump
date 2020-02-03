from collections.abc import Iterable

def flatten_iterable(nested_list):
    """Flatten any nested iterable (not just lists)"""
    result = []

    def _flatten(item):
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            for subitem in item:
                _flatten(subitem)
        else:
            result.append(item)

    _flatten(nested_list)
    return result

# Example
nested = [1, (2, [3, 4]), {5, 6}, "hello"]
result = flatten_iterable(nested)
print(result)  # [1, 2, 3, 4, 5, 6, 'hello']
