def recursive_bin_search(lst: list, target, left: int, right: int):
    if left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            return recursive_bin_search(lst, target, mid, right)
        else:
            return recursive_bin_search(lst, target, left, mid)
    else:
        # element not found
        return -1


def binary_search(lst: list, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # target not found


arr = list(map(int, input().strip().split()))
flag = int(input())
print(recursive_bin_search(arr, flag, 0, len(arr) - 1))
