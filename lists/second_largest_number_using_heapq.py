import heapq

def second_largest_heapq(lst):
    """Using heapq module"""
    if len(lst) < 2:
        return None

    # Get two largest distinct elements
    largest_two = heapq.nlargest(2, set(lst))

    if len(largest_two) >= 2:
        return largest_two[1]
    return None

# Example
numbers = [10, 20, 4, 45, 99]
result = second_largest_heapq(numbers)
print(result)  # 45
