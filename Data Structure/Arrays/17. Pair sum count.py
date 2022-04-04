# Input: arr[] = {1, 5, 7, -1}, k = 6
# Output: 2
# Pairs with sum 6 are (1, 5) and (7, -1)
#
# SOL 1: Naive using nested loop O(n^2)
# SOL 2: Using Map O(n)
# SOL 3: merge sort technique O(n Log n).Needs to sort array
#
from collections import defaultdict


# O(N) , O(N)
def pairSumMap(arr, sum):
    map = set()

    for val in arr:
        if sum - val in map:
            print(sum - val, val)
        else:
            map.add(val)


# O(n logN), O(N)
def pairSum(arr, k):
    arr.sort()
    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] + arr[j] == k:
            print(arr[i], arr[j])
            i = i + 1
            j = j - 1
        elif arr[i] + arr[j] < k:
            i = i + 1
        elif arr[i] + arr[j] > k:
            j = j - 1


arr = [int(i) for i in input().strip().split()]
k = int(input())
# ans = pairSum(arr, k)
ans = pairSumMap(arr, k)
