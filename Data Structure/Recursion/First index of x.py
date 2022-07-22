def firstIndex(arr, x):
    res  = firstIndexHelper(arr, x, 0)
    return res


def firstIndexHelper(arr, x, i):
    l = len(arr)
    if l == 0:
        return -1
    if i == l:
        return -1

    if arr[i] == x:
        return i
    else:
        return firstIndexHelper(arr, x, i = i + 1)


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
ans = firstIndex(arr, x)
print(ans)
