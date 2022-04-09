import sys


def minSum(arr, n):
    min_so_far = sys.maxsize
    min_ending_here = sys.maxsize

    for i in range(1, n):
        min_ending_here = min(arr[i], arr[i] + min_ending_here)
        min_so_far = min(min_so_far, min_ending_here)
    return min_so_far


arr = [2, 3, 1, 2, 4, 3]
n = len(arr)
print(minSum(arr, n))
