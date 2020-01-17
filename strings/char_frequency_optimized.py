def char_frequency_optimized(s):
    """Optimized character frequency using array for ASCII characters"""
    # Assuming ASCII extended (256 characters)
    freq = [0] * 256

    for char in s:
        freq[ord(char)] += 1

    # Convert to dictionary
    result = {}
    for i in range(256):
        if freq[i] > 0:
            result[chr(i)] = freq[i]

    return result
