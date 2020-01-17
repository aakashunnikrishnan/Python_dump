def analyze_string_interactive():
    """Interactive string analysis tool"""
    print("String Character Analysis Tool")
    print("=" * 50)

    while True:
        s = input("\nEnter a string (or 'quit' to exit): ")

        if s.lower() == 'quit':
            print("Goodbye!")
            break

        if not s:
            print("Empty string entered")
            continue

        print(f"\nAnalysis of: '{s}'")
        print("-" * 30)

        # Basic analysis
        print("1. Character Frequency:")
        freq = char_frequency(s)
        for char, count in sorted(freq.items()):
            print(f"   '{char}': {count}")

        print("\n2. Frequency Distribution:")
        # Group by frequency
        freq_dist = {}
        for char, count in freq.items():
            if count in freq_dist:
                freq_dist[count].append(char)
            else:
                freq_dist[count] = [char]

        for count in sorted(freq_dist.keys(), reverse=True):
            chars = freq_dist[count]
            print(f"   {count} occurrence{'s' if count > 1 else ''}: {chars}")

        print("\n3. Most Frequent Character(s):")
        most_chars, most_count = most_frequent_chars(s)
        if len(most_chars) == 1:
            print(f"   '{most_chars[0]}' appears {most_count} times")
        else:
            print(f"   Characters {most_chars} appear {most_count} times each")

        print("\n4. Least Frequent Character(s):")
        least_chars, least_count = least_frequent_chars(s)
        if len(least_chars) == 1:
            print(f"   '{least_chars[0]}' appears {least_count} time{'s' if least_count > 1 else ''}")
        else:
            print(f"   Characters {least_chars} appear {least_count} time{'s' if least_count > 1 else ''} each")

        print("\n5. String without Duplicates:")
        print(f"   '{remove_duplicates(s)}'")

        print("\n6. Duplicate Characters:")
        duplicates = find_all_duplicates(s)
        if duplicates:
            for char, count in sorted(duplicates.items()):
                print(f"   '{char}' appears {count} times")
        else:
            print("   No duplicates found")

        print("\n7. Character Statistics:")
        unique_chars = len(freq)
        total_chars = sum(freq.values())
        duplicate_chars = len(duplicates)
        print(f"   Total characters: {total_chars}")
        print(f"   Unique characters: {unique_chars}")
        print(f"   Duplicate characters: {duplicate_chars}")
        print(f"   Unique/Total ratio: {unique_chars/total_chars:.2%}")
