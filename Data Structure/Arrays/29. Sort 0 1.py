# NAIVE N*N:
def SortZeroOne(arr):
    for i in range(len(arr)):
        if (arr[i] == 1):
            for j in range(i + 1, len(arr)):
                if (arr[j] == 0):
                    arr[j], arr[i] = arr[i], arr[j]


# EFFICIENT : O(N)
# counting zero's and one's and the assigning

n = int(input())
arr = [int(i) for i in input().split()]
SortZeroOne(arr)
print(arr)
