n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
flag = 0
for i in range(m):
    flag += arr[i]
print(flag)