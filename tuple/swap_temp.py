def swap_temp(a, b):
    """Swap using temporary variable (for comparison)"""
    temp = a
    a = b
    b = temp
    return a, b

# Example
x, y = 5, 10
x, y = swap_temp(x, y)
print(f"Temp method: x={x}, y={y}")
