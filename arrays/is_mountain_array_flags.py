def is_mountain_array_flags(arr):
    """Check mountain array using state flags"""
    if len(arr) < 3:
        return False

    increasing = True
    found_peak = False

    for i in range(len(arr) - 1):
        if increasing:
            if arr[i] < arr[i + 1]:
                continue
            elif arr[i] > arr[i + 1]:
                # Started decreasing, found peak
                increasing = False
                found_peak = True
            else:
                # Equal elements not allowed
                return False
        else:
            # In decreasing phase
            if arr[i] > arr[i + 1]:
                continue
            else:
                # Should be strictly decreasing, any plateau or increase is invalid
                return False

    # Must have found a peak at some point
    return found_peak

# Example
arr1 = [1, 2, 3, 2, 1]
arr2 = [0, 3, 2, 1]  # Valid
arr3 = [1, 2, 3, 4]  # No peak (strictly increasing)
print(is_mountain_array_flags(arr1))  # True
print(is_mountain_array_flags(arr2))  # True
print(is_mountain_array_flags(arr3))  # False
