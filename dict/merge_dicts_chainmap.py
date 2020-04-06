from collections import ChainMap

def merge_dicts_chainmap(dict1, dict2):
    """ChainMap (doesn't sum, shows first occurrence)"""
    # This returns first occurrence, not sum
    return dict(ChainMap(dict2, dict1))

# For summing, we still need custom logic
def merge_dicts_chainmap_sum(dict1, dict2):
    """Manual merge using ChainMap concepts"""
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result

# Example
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 1, 'd': 4}
result = merge_dicts_chainmap_sum(dict1, dict2)
print(result)
