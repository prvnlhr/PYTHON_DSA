import sys


# Write an efficient program to find the sum of contiguous subarray within a
# one-dimensional array of numbers that has the largest sum.

# Kadane’s Algorithm:
#
# Initialize:
#     max_so_far = INT_MIN
#     max_ending_here = 0
#
# Loop for each element of the array
#   (a) max_ending_here = max_ending_here + a[i]
#   (b) if(max_so_far < max_ending_here)
#             max_so_far = max_ending_here
#   (c) if(max_ending_here < 0)
#             max_ending_here = 0
# return max_so_fa

#
# Explanation:
# The simple idea of Kadane’s algorithm is to look for all positive contiguous
# segments of the array (max_ending_here is used for this). And keep track of
# maximum sum contiguous segment among all positive segments (max_so_far is used for this).
# Each time we get a positive-sum compare it with max_so_far and update max_so_far if it is greater than max_so_far

# Lets take the example:
#   {-2, -3, 4, -1, -2, 1, 5, -3}
#
#   max_so_far = max_ending_here = 0
#
#   for i = 0,  a[0] =  -2
#   max_ending_here = max_ending_here + (-2)
#   Set max_ending_here = 0 because max_ending_here < 0
#
#   for i=1,  a[1] =  -3
#   max_ending_here = max_ending_here + (-3)
#   Set max_ending_here = 0 because max_ending_here < 0
#
#   for i=2,  a[2] =  4
#   max_ending_here = max_ending_here + (4)
#   max_ending_here = 4
#   max_so_far is updated to 4 because max_ending_here greater
#   than max_so_far which was 0 till now
#
#   for i=3,  a[3] =  -1
#   max_ending_here = max_ending_here + (-1)
#   max_ending_here = 3
#
#   for i=4,  a[4] =  -2
#   max_ending_here = max_ending_here + (-2)
#   max_ending_here = 1
#
#   for i=5,  a[5] =  1
#   max_ending_here = max_ending_here + (1)
#   max_ending_here = 2
#
#   for i=6,  a[6] =  5
#   max_ending_here = max_ending_here + (5)
#   max_ending_here = 7
#   max_so_far is updated to 7 because max_ending_here is
#   greater than max_so_far
#
#   for i=7,  a[7] =  -3
#   max_ending_here = max_ending_here + (-3)
#   max_ending_here = 4


# This is optimized best solution:: O(n) O(1)
def maxSum(arr, n):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, n):
        max_ending_here = max(arr[i], arr[i] + max_ending_here)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

    # def maxSum1(arr, n):
    #     max_so_far = arr[0]
    #     max_ending_here = arr[0]
    #     start = 0
    #     end = 0
    #     s = 0
    #
    #     for i in range(1, n):
    #         currMaxEndingHere = max_ending_here + arr[i]
    #         if arr[i] < currMaxEndingHere:
    #             max_ending_here = currMaxEndingHere
    #         elif arr[i] > currMaxEndingHere:
    #             max_ending_here = arr[i]
    #
    #         if max_so_far < max_ending_here:
    #             max_so_far = max_ending_here
    #             start = s
    #             end = i
    #             s = i + 1

    # print(max_so_far)
    # return start, end
    # arr = [int(i) for i in input().strip().split()]


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
n = len(arr)
print(maxSum(arr, n))
