def left_rotate_by_n(arr: list, n: int) -> list:
    flag = n % len(arr)
    lst = arr[:flag]
    for i in range(flag):
        arr.remove(arr[0])
    arr.extend(lst)
    return arr


print(left_rotate_by_n([1, 2, 3, 4, 5, 6, 7], 83))
