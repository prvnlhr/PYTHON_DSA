# Naive solution will be to use merge sort's, merge technique
# to find combined array and then find median.
# As for combined array we use extra array of size(m+n)
# we can further optimised by just keeping pointer without actually
# storing the elements.
# ________________


# _______________________
import sys


def medianOfSortedArrays(arr1, arr2):
    if len(arr1) > len(arr2):
        medianOfSortedArrays(arr2, arr1)
    m = len(arr1)
    n = len(arr2)
    low = 0
    high = m
    while low <= high:
        # arr1 =  7 12 14 15 , m = 4
        # arr2 = 1 2 3 4 9 11 , n = 6

        #   lo                            hi
        #   |             |                |
        #   0  1  2  3  4 | 5  6   7   8   9
        #   1  2  3  4  7 | 9  11  12  14  15
        #                 |

        # total elements in sorted array is = m + n => 10
        # so median will be (m+n) //2 = 5
        # how much elements at max can be taken from arr1?? -> 4
        # so let say len(m)//2 => 2 , we take 2 elements from arr1
        # so remaining elements that need to be taken from arr2 will be 5-2 = 3
        # Hence cut1 = m//2
        # cut2 = m+n+1 //2 - cut1

        cut1 = (low + high) // 2  # Elements to consider from 1st array
        cut2 = (m + n + 1) // 2 - cut1  # Elements to consider from 2nd array

        left1 = float("-inf") if cut1 == 0 else arr1[cut1 - 1]
        left2 = float("-inf") if cut2 == 0 else arr2[cut2 - 1]

        right1 = float("inf") if cut1 == m else arr1[cut1]
        right2 = float("inf") if cut2 == n else arr2[cut2]
        if left1 <= right2 and left2 <= right1:
            if (m + n) % 2 == 0:
                ans = max(left1, left2) + min(right1, right2)
                return ans / 2.0
            else:
                return max(left1, left2)

        elif left1 > right2:
            high = cut1 - 1
        elif left2 > right1:
            low = cut1 + 1


# Efficient solution , using binary search technique
# This solution is optimised but a bit of tricky

# T: O(min(log m, log n))
# S : O(1)

def medianOfSortedArrays(arr1, arr2):
    if len(arr1) > len(arr2):
        medianOfSortedArrays(arr2, arr1)

    m = len(arr1)
    n = len(arr2)

    low = 0
    high = m

    # Total elements in a sorted array will be m + n
    # if m = 4 , n = 6 , total element will be , 10
    #  if we do partition we will get 5 elements in one and 5 in other
    # Now what is mid of first array of len 4 ?? 4 //2 = 2
    # so if we took 2 elements from first array , then how much we took from second array , 5 - 2 =  3

    # arr1 =  7 12 14 15 , m = 4
    # arr2 = 1 2 3 4 9 11 , n = 6
    # sorted array  =  1 2 3 4 7 9 11 12 14 15
    # mid of first array 4//2 = 2
    #
    # so if we consider 2 ele from 1st array , then we need to consider 5 - 2 elements from 2nd array
    #
    # 1st arr ele ->  2 ele    7  12     |  14  15
    #  2nd arr ele -> 3 ele    1  2  3   |   4   9  11

    # left1 = 12 ,left2 = 3
    # right1 = 14 , right2 = 4

    # now, if at any point, left1 <= right2 and left2 <= right1:
    # we have our median as { max(left1,left2) + min(right1,right2) } // 2.0

    # else if left1 >  right2:  left - 1
    # else if left1

    while low <= high:

        # Now consider the combination of both the array,

        #   lo                            hi
        #   |                             |
        #   0  1  2  3  4  5  6   7   8   9
        #   1  2  3  4  7  9  11  12  14  15

        # lo = 0 , hi = 9
        # cut or cut1 will be at (lo + hi)//2  == 0 + 9 = 9//2 = 4

        # so we will consider 4 elements from 1st array
        # Now, How much elements to consider from 2nd array ??

        # Total elements in combined array is 10 == (ele in 1st )m + (ele in 2nd)n

        # so (m + n - cut1)  will be elements to consider from 2nd array
        # Now we are taking m + n + 1 , because we want to cut the array equal so one step further

        cut1 = (low + high) // 2  # Elements to consider from 1st array
        cut2 = (m + n + 1) // 2 - cut1  # Elements to consider from 2nd array

        # We want to make cut at cut1-1 , but if cut1 ==0 ,
        # cut1 -1 = 0-1 = -1, so we can make cut at arr[-1]
        # so we take it as '-inf'
        left1 = float("-inf") if cut1 == 0 else arr1[cut1 - 1]
        left2 = float("-inf") if cut2 == 0 else arr2[cut2 - 1]

        right1 = float("inf") if cut1 == m else arr1[cut1]
        right2 = float("inf") if cut2 == n else arr2[cut2]
        print(left1, right1)
        print(left2, right2)
        print()
        if left1 <= right2 and left2 <= right1:
            if (m + n) % 2 == 0:
                # print(left1, left2, right1, right2)

                ans = max(left1, left2) + min(right1, right2)
                return ans / 2.0
            else:
                return max(left1, left2)

        elif left1 > right2:
            high = cut1 - 1

        elif left2 > right1:
            low = cut1 + 1


def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)

    left_size = (m + n + 1) // 2

    start = 0
    end = m
    is_even = ((m + n) % 2) == 0
    while start <= end:
        partitionX = (start + end) // 2
        partitionY = left_size - partitionX

        left1 = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
        left2 = float("-inf") if partitionY == 0 else nums2[partitionY - 1]

        right1 = float("inf") if partitionX == m else nums1[partitionX]
        right2 = float("inf") if partitionY == n else nums2[partitionY]

        if left1 <= right2 and left2 <= right1:
            if not is_even:
                return max(left1, left2)
            else:
                return (max(left1, left2) + min(right1, right2)) / 2.0
        elif left1 > right2:
            end = partitionX - 1
        elif left2 > right1:
            start = partitionX + 1


arr1 = [7, 12, 14, 15]
arr2 = [1, 2, 3, 4, 9, 11]

# arr1 = [int(i) for i in input().strip().split()]
# arr2 = [int(j) for j in input().strip().split()]
print(medianOfSortedArrays(arr1, arr2))
