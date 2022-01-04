import sys


# Time Complexity O(1/2 * N) => O(N) because , 1/2 is constant


def findMaxMin(arr):
    min = sys.maxsize
    max = ~sys.maxsize
    print(min, max)
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    return min, max


arr = [int(i) for i in input().strip().split()]
ans = findMaxMin(arr)
print(ans)
