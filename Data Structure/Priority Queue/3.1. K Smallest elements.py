import heapq

def kSmallest(lst , k):
        maxHeap = lst[:k]
        heapq._heapify_max(maxHeap)
        n = len(lst)
        for i in range(k,n):
            if lst[i]<maxHeap[0]:
                heapq._heapreplace_max(maxHeap , lst[i])
        return maxHeap
