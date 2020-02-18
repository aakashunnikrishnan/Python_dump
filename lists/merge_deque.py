from collections import deque

def merge_deque(list1, list2):
    """Merge using deques for efficient left popping"""
    dq1 = deque(list1)
    dq2 = deque(list2)
    merged = []

    while dq1 and dq2:
        if dq1[0] <= dq2[0]:
            merged.append(dq1.popleft())
        else:
            merged.append(dq2.popleft())

    merged.extend(dq1)
    merged.extend(dq2)

    return merged

# Example
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = merge_deque(list1, list2)
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8]
