def left_rotate_array(arr: list) -> list:
    n = arr[0]
    arr.remove(n)
    arr.append(n)
    return arr


print(left_rotate_array([1, 2, 3, 4, 5, 6]))
