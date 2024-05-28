def subarray_sum(arr: list[int], n: int, sum_: int) -> list:
    curr_sum = arr[0]
    start = 0
    i = 1
    while i <= n:

        while curr_sum > sum_ and start < i - 1:
            curr_sum = curr_sum - arr[start]
            start += 1

        if curr_sum == sum_:
            return [start+1, i]

        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1

    return [-1]


print(subarray_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n=10, sum_=15))
