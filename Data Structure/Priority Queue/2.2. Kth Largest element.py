import heapq


# Note: Try to do this question in less than O(N * logN) time
# Sample Input 1 :
# 6
# 9 4 8 7 11 3
# 2
# Sample Output 1 :
# 9
# Sample Input 2 :
# 8
# 2 6 10 11 13 4 1 20
# 4
# Sample Output 2 :
# 10


# Easy would be to sort array using merge sort which would give O(NlogN) time complexity.

# Better implementation would be to use heap


# INCORRECT INTUITION__
# one might think if we just heapify the input list and give the kth element from  end as heapify,
# would arrange the list in decreasing order. But HEAPIFY does not sort the lst, it just bring the,
# smallest element at top.

# CORRECT INTUITION__
# 1. put k element in heap and heapify them.
# 2. now run the loop from k to len(lst) k --> n.
# 3. push a element to heap which will then maintain the heap order by bringing he smallest at top.
# 4. pop the element from heap.
# 5 . repeat the process and at end only k largest element will be left in heap with.
# 6 . kth largest will be at top [0] index.


# O(N log k)
def kthLargest(lst, k):
    heap = lst[:k]
    heapq.heapify(heap)
    for i in range(k, len(lst)):
        heapq.heappush(heap, lst[i])
        heapq.heappop(heap)

    return heap[0]


n = int(input())
arr = [int(i) for i in input().strip().split()]
k = int(input())
ans = kthLargest(arr, k)
print(ans)
