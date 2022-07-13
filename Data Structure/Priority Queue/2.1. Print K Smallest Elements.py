# You are given with an integer k and an array of integers that contain
# numbers in random order. Write a program to find k smallest numbers from given array.
# You need to save them in an array and return it.
# Time complexity should be O(n * logK) and space complexity should not be more than O(k).
# Note: Order of elements in the output is not important.
# Input Format :
# The first line of input contains an integer, that denotes the value of the
# size of the array. Let us denote it with the symbol N.
# The following line contains N space separated integers, that denote the value
# of the elements of the array.
# The following line contains an integer, that denotes the value of k.
# Output Format :
# The first and only line of output print k smallest elements.
# The elements in the output are separated by a single space.
# Constraints:
# Time Limit: 1 sec
# Sample Input 1 :
# 13
# 2 12 9 16 10 5 3 20 25 11 1 8 6
# 4
# Sample Output 1 :
# 1 2 3 5


# NOTE: if we sort elements and then find k smallest,
# time complexity will be , O(nlogN)

# using a max_heap we can do it efficiently

# STEPS__:
# 1. take k elements in a max_heap arr from input list
# 2. do, heapq.heapify_max(max_heap), which will sort it in decreasing order.
# 3. now for the rest of elements in input list run a loop from i = k --> n and compare ,
# list[i] and max_heap[0] elements, if list[i] element is smaller then replace,
# then replace it in max_heap.
# 5. at end after loop we will get all k smallest element in max_heap.

import heapq

'''HEAP TIME COMPLEXITY ANALYSIS

PUSH : O(log n)
POP : O(log n)

# 
Algorithm	    Average	   Worst case
Space		    O(n)	   O(n)
Search		    O(n)	   O(n)
Insert		    O(1)	   O(log n)
Find-min	    O(1)	   O(1)
Delete-min	    O(log n)   O(log n)

'''


# __CN Solution
def kSmallest(lst, k):
    maxHeap = lst[:k]
    print(maxHeap)
    # heapify_max is heapq functionality which creates max_heap with largest element at first

    # O(K logK)
    heapq._heapify_max(maxHeap)
    print(maxHeap)
    n = len(lst)

    for i in range(k, n):  # (N-k) times
        print(lst[i], maxHeap[0])
        if lst[i] < maxHeap[0]:
            heapq._heapreplace_max(maxHeap, lst[i])  # logK
    print(maxHeap)

    # overall time Complexity : (n-K)logK + K logK => n LogK
    return maxHeap


# Self solved__. passes 100% test cases on CN, but don't know if appropriate.
def printKSmallest(arr, k):
    heapq.heapify(arr)
    ans = []
    for i in range(k):
        ans.append(heapq.heappop(arr))
    return ans


n = int(input())
arr = [int(i) for i in input().strip().split()]
k = int(input())
# ans = printKSmallest(arr, k)
ans = kSmallest(arr, k)
print(ans)
