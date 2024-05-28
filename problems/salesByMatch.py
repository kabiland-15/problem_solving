def find_pair_of_socks(socks: list) -> int:
    lst1 = set(socks)
    a = 0
    for i in lst1:
        a += socks.count(i)//2
    return a


n = int(input().strip())
lst = list(map(int, input().strip().split()))
result = find_pair_of_socks(lst)
print(result)
