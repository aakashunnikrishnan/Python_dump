def swap_tuple_assignment(a, b):
    """Swap two numbers using tuple assignment (packing/unpacking)"""
    a, b = b, a
    return a, b

# Example
x, y = 5, 10
print(f"Before swap: x={x}, y={y}")
x, y = swap_tuple_assignment(x, y)
print(f"After swap: x={x}, y={y}")  # x=10, y=5
