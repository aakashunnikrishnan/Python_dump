# Example: Lists manipulation
def list_operations():
    n = int(input())
    arr = list(map(int, input().split()))

    # Common operations
    arr.append(5)
    arr.insert(2, 10)
    arr.remove(3)
    return arr
