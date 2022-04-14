from collections import defaultdict


# ANUJ'S YT VIDEO::

# AS WE HAVE TO FIND A SUB ARRAY WITH GIVEN SUM,
# IT WOULD HAVE BEEN EASY TO FIND IF ALL ELEMENTS IN ARRAY WOULD HAVE BEEN POSITIVE
# BUT SINCE ELEMENTS CAN BE NEGATIVE,
# WE CANT USE THE APPROACH IN PROBLEM NO 42.
# THE NAIVE APPROACH TO THIS PROBLEM WOULD BE TO FIND ALL SUB ARRAY
# WHICH WOULD COST N*N TIME COMPLEXITY

# WE CAN OPTIMISE WITH USING HASHMAP
# APPROACH::
# for every element in array find currSum, if currSum == sum, we have sub array from 0 to i
# otherwise we put currSum and currIndex to map as key and value.

# Now if map has value equal to  curSum - sum , then from index value from map[currSum - sum] to currIndex is our ans


def subarray(arr, s):
    map = defaultdict(list)

    currSum = 0

    for i, ele in enumerate(arr):

        currSum += ele

        if currSum == s:
            return 0, i

        if currSum - s in map:
            res = (map[currSum - s] + 1, i)
            return res

        map[currSum] = i

    return -1, -1


testCases = [[[10, 2, -2, -20, 10], [-10]], [[15, 2, 4, 8, 9, 5, 10, 23], [23]], [[-10, 0, 2, -2, -20, 10], [20]]]
for arr, sum in testCases:
    print(arr, sum[0])
    ans = subarray(arr, sum[0])
    print(arr[ans[0]:ans[1] + 1])
    print()
