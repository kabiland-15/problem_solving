arr = [10, 20, 30, 40, 50, 60, 70, 80]
target = 70
left = 0
right = len(arr)

while left < right:
    mid = (left + right) // 2
    if arr[mid] > target:
        right = mid
    elif arr[mid] < target:
        left = mid
    else:
        print(mid)
        break
