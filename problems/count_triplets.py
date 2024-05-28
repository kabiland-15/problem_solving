def count_triplets(arr: list, n: int) -> int:
    arr.sort()
    count = 0
    i = n-1
    while i >= 0:
        j = 0
        k = i-1
        while j < k:
            if arr[k] + arr[j] == arr[i]:
                count += 1
                j += 1
                k -= 1
            elif arr[k] + arr[j] > arr[i]:
                k -= 1
            else:
                j += 1
        i -= 1
    return count


print(count_triplets([5, 4, 3, 2, 1], 5))
