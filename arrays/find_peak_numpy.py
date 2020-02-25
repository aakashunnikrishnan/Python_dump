import numpy as np

def find_peak_numpy(nums):
    """Find peaks using numpy (returns all peaks)"""
    if not nums:
        return []

    arr = np.array(nums)

    # Find peaks where element > neighbors
    peaks = np.where((arr[1:-1] > arr[:-2]) & (arr[1:-1] > arr[2:]))[0] + 1

    # Check boundaries
    if len(arr) > 1 and arr[0] > arr[1]:
        peaks = np.append([0], peaks)
    if len(arr) > 1 and arr[-1] > arr[-2]:
        peaks = np.append(peaks, len(arr) - 1)

    return peaks.tolist()

# Example
numbers = [1, 3, 2, 5, 4, 6, 1]
result = find_peak_numpy(numbers)
print(f"Numpy peaks at indices: {result}")
