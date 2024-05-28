lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
j = len(lst)-1
for i in range(len(lst)//2):
    lst[i] = lst[j-i]
print(lst)
