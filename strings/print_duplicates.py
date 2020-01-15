def print_duplicates(s):
    """Print duplicate characters in a string"""
    freq = char_frequency(s)
    duplicates = []

    for char, count in freq.items():
        if count > 1:
            duplicates.append(char)

    if duplicates:
        print("Duplicate characters:", end=" ")
        for char in duplicates:
            print(f"'{char}'", end=" ")
        print(f"({len(duplicates)} total)")
    else:
        print("No duplicate characters found")
