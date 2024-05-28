def swap_string(s: list, n: int) -> list:
    i = 0
    j = n-1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s


s1 = [1, 2, 3, 4, 5]
print(swap_string(s1, len(s1)))
