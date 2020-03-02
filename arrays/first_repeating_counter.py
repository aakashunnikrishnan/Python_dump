from collections import Counter

def first_repeating_counter(arr):
    """Find first repeating element using Counter"""
    freq = Counter(arr)

    for num in arr:
        if freq[num] > 1:
            return num

    return None

# Example
arr = [10, 5, 3, 4, 3, 5, 6]
result = first_repeating_counter(arr)
print(f"First repeating element: {result}")  # 3
