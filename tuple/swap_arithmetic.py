def swap_arithmetic(a, b):
    """Swap using addition and subtraction (works for numbers)"""
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Example
x, y = 5, 10
x, y = swap_arithmetic(x, y)
print(f"Arithmetic: x={x}, y={y}")
