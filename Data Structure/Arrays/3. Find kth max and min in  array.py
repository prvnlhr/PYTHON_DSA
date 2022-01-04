import heapq
import sys


# Naive easy solution would be to solve using merge sort.
# Merge sort would take O(N logN) time and we can find kth
# smallest and kth largest from sorted array which will
# take O(1) time. So overall time complexity would be O(N logN) ,neglecting constant time.

def findKthMaxMin(arr, k):
    arr = sorted(arr)
    print(arr)
    n = len(arr)
    kthSmallest = arr[k - 1]
    kthLargest = arr[n - k]
    print(kthSmallest, kthLargest)


# Optimize solution using Heaps:
# Both findKthMin ,findKthMax are optimize using heap
# Time Complexity : N log K which it better then O(N log N)
def findKthMin(arr, k):
    maxHeap = []
    for i in range(0, k):
        maxHeap.append(arr[i])
    heapq._heapify_max(maxHeap)
    for i in range(k, len(arr)):
        if arr[i] < maxHeap[0]:
            # replace max heap element
            heapq._heapreplace_max(maxHeap, arr[i])
    print(maxHeap[0])
    return maxHeap[0]


def findKthMax(arr, k):
    minHeap = []
    for i in range(0, k):
        minHeap.append(arr[i])
    heapq.heapify(minHeap)
    # print(minHeap)
    for i in range(k, len(arr)):
        # print(minHeap)
        if minHeap[0] < arr[i]:
            heapq.heapreplace(minHeap, arr[i])
    print(minHeap[0])
    return minHeap[0]


# 7 10 4 3 20 15
# k = 3   o/p-> 7
arr = [int(i) for i in input().strip().split()]
k = int(input())
ans = findKthMax(arr, k)
