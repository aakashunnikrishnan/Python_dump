def find_pairs_two_pointer(lst, target):
    """Find all pairs using two-pointer technique (list must be sorted)"""
    lst_sorted = sorted(lst)
    left = 0
    right = len(lst_sorted) - 1
    pairs = []

    while left < right:
        current_sum = lst_sorted[left] + lst_sorted[right]

        if current_sum == target:
            pairs.append((lst_sorted[left], lst_sorted[right]))
            left += 1
            right -= 1

            # Skip duplicates
            while left < right and lst_sorted[left] == lst_sorted[left - 1]:
                left += 1
            while left < right and lst_sorted[right] == lst_sorted[right + 1]:
                right -= 1

        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs

# Example
numbers = [7, 2, 5, 3, 1, 6, 4]
target = 8
result = find_pairs_two_pointer(numbers, target)
print(result)  # [(1, 7), (2, 6), (3, 5)]
