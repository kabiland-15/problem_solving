def single_number(lst: list) -> int:
    xor = 0
    for i in lst:
        xor ^= i
    return xor


print(single_number([1, 1, 1, 2, 2, 3]))
