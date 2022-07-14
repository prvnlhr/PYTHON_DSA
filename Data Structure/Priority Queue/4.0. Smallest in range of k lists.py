import sys
from heapq import *
from hmac import new

'''
Given k sorted lists of integers of size n each, find the smallest range that 
includes at least element from each of the k lists. If more than one smallest 
ranges are found, print any one of them.

Input: K = 3
arr1[] : [4, 7, 9, 12, 15]
arr2[] : [0, 8, 10, 14, 20]
arr3[] : [6, 12, 16, 30, 50]
Output:
The smallest range is [6 8]

Explanation: Smallest range is formed by 
number 7 from the first list, 8 from second
list and 6 from the third list.

Input: k = 3
arr1[] : [4, 7]
arr2[] : [1, 2]
arr3[] : [20, 40]
Output:
The smallest range is [2 20]

Explanation:The range [2, 20] contains 2, 4, 7, 20
which contains element from all the three arrays.

'''


# 1. Initialize next array(pointers) with all 0's.
# 2. (finding the minimum value iteratively at every step) Find the indices
#    of the lists containing the minimum(min(i) and the maximum(max(i))
#    elements amongst the elements pointed by the next array.
# 3. If the range formed by the maximum and minimum elements found above
#    is larger than the previous maximum range, update the boundary values used for the maximum range.
# 4. Increment the pointer nums[min(i)]
# 5. Repeat steps 2 to 4 till any of the lists gets exhausted.
#
# To avoid this iterative process, a better idea is to make use of a Min-Heap,
# which stores the values being pointed currently by the next array.
# Thus, the minimum value always lies at the top of this heap, and we
# need not do the iterative search process.
def smallestInRange1(nums):
    minHeap = []
    MIN = sys.maxsize
    MAX = -sys.maxsize

    for i, arr in enumerate(nums):
        heappush(minHeap, (arr[0], i, 0))
        MIN = min(MIN, arr[0])
        MAX = max(MAX, arr[0])

    res = [None] * 1
    new_max = MAX
    existing_range = MAX - MIN
    while minHeap:
        val, i, j = heappop(minHeap)

        if j + 1 >= len(nums[i]):
            return res

        next_ele = nums[i][j + 1]

        heappush(minHeap, (next_ele, i, j + 1))

        new_min = minHeap[0][0]

        new_max = max(new_max, next_ele)
        print(new_min, new_max)

        new_range = new_max - new_min
        print(existing_range)

        if new_range <= existing_range:
            res[0] = (new_min, new_max)
            existing_range = new_range
    return res


class Solution1:
    # At every step, we remove the minimum element from this heap and find
    # out the range formed by the current maximum and minimum values, and compare it
    # with the minimum range found so far to determine the required
    # minimum range.We also update the increment the index in next
    # corresponding to the list containing this minimum entry and add this
    # element to the heap as well.

    def smallestInRange(self, nums):

        # STEP 1: Maintain minHeap and MIN and MAX value for tracking range
        minHeap = []
        MIN = sys.maxsize
        MAX = -sys.maxsize

        # STEP 2: Put all the first elements from all list along with i,j position into heap
        # also update MIN and MAX value
        for i, arr in enumerate(nums):
            # print(arr)
            heappush(minHeap, (arr[0], i, 0))
            MIN = min(MIN, arr[0])
            MAX = max(MAX, arr[0])

        # res stores range start and end
        res = [MIN, MAX]
        # range to store range difference
        range = MAX - MIN
        max_end = MAX

        # STEP 3:
        # till heap does not exhaust,
        # pop element from minHeap,which will give minValue

        while minHeap:

            val, i, j = heappop(minHeap)  # pop element from minHeap , which will give minValue
            next_index = j + 1
            # if next_index does not exist in pop element's list, i.e list exhausted,return res
            if next_index >= len(nums[i]):
                return res

            # if next_index exists, push to minHeap
            heappush(minHeap, (nums[i][next_index], i, next_index))

            # now compare new_range from previous range formed from MIN ,MAX
            new_min = minHeap[0][0]
            max_end = max(max_end, nums[i][next_index])
            # print(new_min, max_end)

            new_range = max_end - new_min
            # if new_range is smaller then old range update and update res
            if new_range < range:
                res = [new_min, max_end]
                range = new_range

        return res

class Solution:
    def smallestInRange(self, nums):
        minHeap = []
        MIN = sys.maxsize
        MAX = -sys.maxsize
        for i, arr in enumerate(nums):
            print('x',arr[0], i, 0)
            heappush(minHeap, (arr[0], i, 0))
            MIN = min(MIN, arr[0])
            MAX = max(MAX, arr[0])
        res = [MIN, MAX]
        range = MAX - MIN
        max_end = MAX
        while minHeap:
            val, i, j = heappop(minHeap)
            print()
            print('y',val,i,j)
            next_index = j + 1
            if next_index >= len(nums[i]):
                return res
            heappush(minHeap, (nums[i][next_index], i, next_index))

            print("z",max_end)
            new_min = minHeap[0][0]
            max_end = max(max_end, nums[i][next_index])
            new_range = max_end - new_min

            # print("z",new_min,max_end,new_range)
            if new_range < range:
                res = [new_min, max_end]
                range = new_range
            print()
            # print('z',res[0],res[1])
        return res
obj = Solution()

# matrix = [[4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]]
# matrix =[[10,10],[11,11]]
# matrix = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
matrix =[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]

# k = 3
ans = obj.smallestInRange(matrix)
# ans1 = smallestInRange1(matrix)
print(ans)
#
# 4 8
# 6 8
# 7 12
# 8 12
# 9 12
# 10 12
# 12 14
# 12 15
# 14 16
# 15 20
# [6, 8]
