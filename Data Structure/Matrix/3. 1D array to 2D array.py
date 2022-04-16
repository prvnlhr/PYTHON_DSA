def oneDtoTwoD(arr, m, n):
    if m * n != len(arr):
        return []
    res = []
    temp = []

    for i in range(len(arr)):

        temp.append(arr[i])
        if len(temp) == n:
            res.append(temp)
            temp = []
    return res


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
m = 3
n = 3
ans = oneDtoTwoD(arr, m, n)
print(ans)
