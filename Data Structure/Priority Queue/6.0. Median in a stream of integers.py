# Ex__1. 5, 15, 1, 3

# After reading 1st element of stream - 5 -> median - 5
# After reading 2nd element of stream - 5, 15 -> median - 10
# After reading 3rd element of stream - 5, 15, 1 -> median - 5
# After reading 4th element of stream - 5, 15, 1, 3 -> median - 4, so on...
#
# Ex__2. 5 15 1 3 2 8 7 9 10 6 11 4
# median after reading 5 is 5.0
# median after reading 15 is 10.0
# median after reading 1 is 5.0
# median after reading 3 is 4.0
# median after reading 2 is 3.0
# median after reading 8 is 4.0
# median after reading 7 is 5.0
# median after reading 9 is 6.0
# median after reading 10 is 7.0
# median after reading 6 is 6.5
# median after reading 11 is 7.0
# median after reading 4 is 6.5
# Making it clear, when the input size is odd, we take the
# middle element of sorted data. If the input size is even,
# we pick the average of the middle two elements in the sorted stream.


# Method 1: Insertion Sort
# # If we can sort the data as it appears, we can easily locate the
# # median element. Insertion Sort is one such online algorithm that
# # sorts the data appeared so far. At any instance of sorting, say
# # after sorting i-th element, the first i elements of the array are sorted.
# # The insertion sort doesn't’t depend on future data to sort data input till
# # that point. In other words, insertion sort considers data sorted so far
# # while inserting the next element. This is the key part of insertion sort
# # that makes it an online algorithm.
# # However, insertion sort takes O(n2) time to sort n elements.


# EFFICIENT SOL USING HEAP:
# Time Complexity: If we omit the way how stream was read, complexity of
# median finding is O(N log N), as we need to read the stream,
# and due to heap insertions/deletions.
#
# Auxiliary Space: O(N)

# As we read a num from input we put it to heap and find median till that point
from heapq import *


class Solution:

    def __init__(self):
        self.minHeap = []  # store large half, top will be smallest in large part
        self.maxHeap = []  # store small half, top will be largest in small part

    def addNum(self, num):  # IMP

        if len(self.maxHeap) == 0:
            # Note we are using -ve value of num because by default all heap are min heaps,
            # so to make max heap make elements negative
            heappush(self.maxHeap, -num)
            return

        if num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) - len(self.minHeap) == 2:
            heappush(self.minHeap, -heappop(self.maxHeap))

        elif len(self.maxHeap) - len(self.minHeap) == -2:
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self):
        print(self.minHeap)
        print(self.maxHeap)

        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0

        return -float(self.maxHeap[0]) if len(self.maxHeap) > len(self.minHeap) else float(self.minHeap[0])


streamOfIntegers = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
obj = Solution()
for num in streamOfIntegers:
    obj.addNum(num)
    print('median after reading', num, 'is', obj.findMedian())

# []
# [-5]
# median after reading 5 is 5.0
# [15]
# [-5]
# median after reading 15 is 10.0
# [15]
# [-5, -1]
# median after reading 1 is 5.0
# [5, 15]
# [-3, -1]
# median after reading 3 is 4.0
# [5, 15]
# [-3, -1, -2]
# median after reading 2 is 3.0
# [5, 15, 8]
# [-3, -1, -2]
# median after reading 8 is 4.0
# [5, 7, 8, 15]
# [-3, -1, -2]
# median after reading 7 is 5.0
# [7, 9, 8, 15]
# [-5, -3, -2, -1]
# median after reading 9 is 6.0
# [7, 9, 8, 15, 10]
# [-5, -3, -2, -1]
# median after reading 10 is 7.0
# [7, 9, 8, 15, 10]
# [-6, -5, -2, -1, -3]
# median after reading 6 is 6.5
# [7, 9, 8, 15, 10, 11]
# [-6, -5, -2, -1, -3]
# median after reading 11 is 7.0
# [7, 9, 8, 15, 10, 11]
# [-6, -5, -4, -1, -3, -2]
# median after reading 4 is 6.5
#
# Process finished with exit code 0
