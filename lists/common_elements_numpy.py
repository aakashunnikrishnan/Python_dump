import numpy as np

def common_elements_numpy(list1, list2):
    """Find common elements using numpy"""
    return list(np.intersect1d(list1, list2))

# Example
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
result = common_elements_numpy(list1, list2)
print(result)  # [4, 5, 6]
