def sort_four_values(arr):
    low = 0
    mid1 = 0
    mid2 = 0
    high = len(arr) - 1

    while mid2 <= high:
        if arr[mid2] == 0:
            arr[low], arr[mid1], arr[mid2] = arr[mid2], arr[low], arr[mid1]
            low += 1
            mid1 += 1
            mid2 += 1
        elif arr[mid2] == 1:
            arr[mid1], arr[mid2] = arr[mid2], arr[mid1]
            mid1 += 1
            mid2 += 1
        elif arr[mid2] == 2:
            mid2 += 1
        else:
            arr[mid2], arr[high] = arr[high], arr[mid2]
            high -= 1

# Example usage:
arr = [3, 2, 1, 0, 2, 1, 3, 0, 2, 1]
sort_four_values(arr)
print(arr)
