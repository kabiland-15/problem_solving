def is_sorted(arr: list, n: int) -> bool:
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True


print(is_sorted([1, 2, 2, 4, 3], 5))
