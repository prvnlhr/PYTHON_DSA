def binarySearch(arr, x, si, ei):
    print(si , ei)
    if si > ei:
        return -1
    mid = (si + ei) // 2
    if arr[mid] == x:
        return mid
    if arr[mid] > x:
        return binarySearch(arr, x, si, mid - 1)

    else:
        return binarySearch(arr, x, mid + 1, ei)


n = int(input())
arr = list(int(i) for i in input().strip().split())
x = int(input())
print(binarySearch(arr, x, 0, n-1))
