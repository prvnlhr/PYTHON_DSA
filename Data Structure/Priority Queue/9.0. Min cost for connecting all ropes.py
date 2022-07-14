import heapq


# There are given n ropes of different lengths, we need
# to connect these ropes into one rope. The cost to connect
# two ropes is equal to the sum of their lengths. We need
# to connect the ropes with minimum cost.
#
# For example, if we are given 4 ropes of lengths 4, 3, 2, and 6.
# We can connect the ropes in the following ways.
# 1) First, connect ropes of lengths 2 and 3. Now we have
# three ropes of lengths 4, 6, and 5.
# 2) Now connect ropes of lengths 4 and 5. Now we have
# two ropes of lengths 6 and 9.
# 3) Finally connect the two ropes and all ropes have connected.
# Total cost for connecting all ropes is 5 + 9 + 15 = 29.
#
# If we observe the above problem closely, we can notice
# that the lengths of the ropes which are picked first are
# included more than once in total cost. Therefore, the idea
# is to connect the smallest two ropes first and recur for
# the remaining ropes

# Complexity Analysis:
# Time Complexity: O(nLogn), assuming that we use a
# O(nLogn) sorting algorithm. Note that heap operations
# like insert and extract take O(Logn) time.
# Auxiliary Complexity:O(n), The space required to store
# the values in min heap


def minCost(arr):
    min_heap = []
    for ele in arr:
        min_heap.append(ele)
    heapq.heapify(min_heap)

    minCost = 0
    while len(min_heap) > 1:
        a = heapq.heappop(min_heap)
        b = heapq.heappop(min_heap)
        x = a + b
        heapq.heappush(min_heap, x)
        minCost = minCost + x
    return minCost


arr = [int(i) for i in input().strip().split()]
ans = minCost(arr)

print(ans)
