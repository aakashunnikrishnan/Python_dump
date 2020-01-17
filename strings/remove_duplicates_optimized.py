def remove_duplicates_optimized(s):
    """Optimized duplicate removal using boolean array"""
    # Assuming ASCII extended (256 characters)
    seen = [False] * 256
    result = ""

    for char in s:
        idx = ord(char)
        if not seen[idx]:
            seen[idx] = True
            result += char

    return result
