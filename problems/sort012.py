def sort012(arr: list[int]) -> list[int]:
    map1 = {0: 0, 1: 0, 2: 0}
    for i in arr:
        map1[i] += 1
    lst = [0 for _ in range(map1[0])]
    lst.extend([1 for _ in range(map1[1])])
    lst.extend([2 for _ in range(map1[2])])
    return lst


print(sort012([0, 2, 1, 2, 0]))
