def count_vowels(s):
    """Count the number of vowels in a string"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
