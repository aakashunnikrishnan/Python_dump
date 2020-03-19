def swap_xor(a, b):
    """Swap using XOR bitwise operation (integers only)"""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# Example
x, y = 5, 10
x, y = swap_xor(x, y)
print(f"XOR method: x={x}, y={y}")
