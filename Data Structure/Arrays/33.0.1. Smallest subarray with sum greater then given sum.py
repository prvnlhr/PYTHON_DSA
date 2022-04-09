# Given an array of integers and a number x, find the
# smallest subarray with sum greater than the given value.
#
# Examples:
# arr[] = {1, 4, 45, 6, 0, 19}
#    x  =  51
# Output: 3
# Minimum length subarray is {4, 45, 6}
#
# arr[] = {1, 10, 5, 2, 7}
#    x  = 9
# Output: 1
# Minimum length subarray is {10}
#
# arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
#     x = 280
# Output: 4
# Minimum length subarray is {100, 1, 0, 200}
#
# arr[] = {1, 2, 4}
#     x = 8
# Output : Not Possible
# Whole array sum is smaller than 8.
import sys


# T: O(N)
# ONLY VALID FOR POSITIVE INTEGERS.
def smallestSubarray(arr, s):
    currSum = 0
    length = sys.maxsize
    n = len(arr)

    i = 0
    j = 0

    while j < n:

        while currSum <= s and j < n:
            currSum += arr[j]
            j += 1

        while currSum > s and i < n:
            length = min(length, j - i)
            currSum -= arr[i]
            i += 1
    return length


def smallestSubarray1(arr, x):
    sum = 0
    min_length = sys.maxsize
    n = len(arr)

    start, end = 0, 0
    while end < n:

        # find sum until sum is smaller then x
        while sum <= x and end < n:
            sum += arr[end]
            end += 1
        # if sum becomes greater update min_length
        # and also sum window sum
        while sum > x and start < n:
            if end - start < min_length:
                min_length = end - start
            sum -= arr[start]
            start += 1

    return min_length


def findMinLength(arr, x):
    min_length = sys.maxsize
    sum = 0
    leftPtr = 0
    for i, ele in enumerate(arr):
        sum += arr[i]

        while sum >= x:
            min_length = min(min_length, i - leftPtr + 1)
            sum -= arr[leftPtr]
            leftPtr += 1

    # 100 % correct Leetcode passed


# O(N)
def minLengthSubarray(arr, x):
    min_length = sys.maxsize

    leftPtr = 0

    sum = 0

    for i, ele in enumerate(arr):
        sum += arr[i]

        while sum >= x:
            '''
             i - leftPtr + 1  , gives length of current subarray 
            '''

            min_length = min(min_length, i - leftPtr + 1)
            sum -= arr[leftPtr]
            leftPtr += 1
    return min_length if min_length != sys.maxsize else 0


testCases = [[[1, 11, 100, 1, 0, 200, 3, 2, 1, 250], [280]],
             [[1, 10, 5, 2, 7], [9]],
             [[1, 4, 45, 6, 0, 19], [51]],
             [[1, 2, 4], [8]], [[2, 3, 1, 2, 4, 3], [7]], [[1, 2, 3, 4, 5]
                 , [11]]]

for arr, sum in testCases:
    ans = minLengthSubarray(arr, sum[0])
    print(ans)
