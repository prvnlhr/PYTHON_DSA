# Given an array arr[] of integers, find out the maximum
# difference between any two elements such that larger element
# appears after the smaller number.


# Input : arr = {2, 3, 10, 6, 4, 8, 1}
# Output : 8
# Explanation : The maximum difference is between 10 and 2.
#
# Input : arr = {7, 9, 5, 6, 3, 2}
# Output : 2
# Explanation : The maximum difference is between 9 and 7.


# Naive Solution Time Complexity : O(n^2) ___

def maxDiff(arr):
    max_diff = arr[1] - arr[0]
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            curr_diff = arr[j] - arr[i]
            max_diff = max(max_diff, curr_diff)
    return max_diff


# Optimize Solution Time Complexity : O(N) ___

# APPROACH ::
# AS we want  max difference , and we know that max diff can be
# obtained from subtracting max and min element in an array
# SO, at any index element in array, if we could find
# the min element from left of it, and subtract it from it, then we can find the diff
# SO the problem boils down to finding min element from left of a element, and finding diff
#
#                 0    1    2     3    4    5    6
# Consider Ex_  [ 2 ,  3 ,  10 ,  6 ,  4 ,  8 ,  1  ]

# Now to consider i = 0 , 2 , what is max diff over here, well its 2 because there is no smaller to left
# i = 1 , 3 , max diff is 3 -2 = 1
# i = 2 , 10 , max diff is 10 - 2 = 8 , why 10 - 2 , because min on left side is 2
# i = 3 , 6 , max diff is 6 - 2 = 4
# i = 4, 4 , max diff is 4 -2 = 2
# i = 5 , 8 , max diff is 8 - 2 = 6
# i = 6 , 1 max diff is 1 - 2 = -1
# so our ans is 8
#
def maxDiffOptimize(arr):
    max_diff = arr[1] - arr[0]
    min_ele_so_far = arr[0]

    for i in range(1, len(arr)):
        min_ele_so_far = min(min_ele_so_far, arr[i])
        curr_diff = arr[i] - min_ele_so_far
        max_diff = max(max_diff, curr_diff)

        # or
        # curr_diff = arr[i] - min_ele_so_far
        # max_diff = max(max_diff, curr_diff)
        # min_ele_so_far = min(min_ele_so_far, arr[i])

    return max_diff


#
#
testCases = [[2, 3, 10, 6, 4, 8, 1], [7, 9, 5, 6, 3, 2]]
# arr = [int(i) for i in input().strip().split()]
# ans1 = maxDiff(arr)
# print(ans1)
for arr in testCases:
    ans2 = maxDiffOptimize(arr)
    print(ans2)
