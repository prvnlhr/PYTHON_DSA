def checkNumber(arr, x):
    l = len(arr)
    if l == 0:
        return False

    if arr[0] == x:
        return True
    return checkNumber(arr[1:], x)


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(checkNumber(arr, x))
