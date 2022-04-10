# Given an integer array A of size N,
# check if the input array can be split in two parts such that -
# -1. Sum of both parts is equal
# -2. All elements in the input, which are divisible by 5 should be in same group.
# -3. All elements in the input, which are divisible by 3 (but not divisible by 5) should be in other group.
# -4. Elements which are neither divisible by 5 nor by 3, can be put in any group.

# n = 2
# 1 2
# false

# n = 3
# 1 4 3
# true

# SOLUTION::
# maintain two variable leftSum and rightSum and iterator i

# if arr[i] is divisible by 3 , rightSum = rightSum + arr[i] and i = i + 1
# if arr[i] is divisible by 5 , leftSum = leftSum + arr[i]  and  i = i + 1
# if arr[i] is neither divisible by 5 or 3, then leftSum + arr[i] and rightSum + arr[i] and check further,

# Time Complexity: O(2 ^ N)
# Auxiliary Space: O(N)
def divideArrayIntoTwoHelper(arr, n, leftSum, rightSum, i):
    if i == len(arr):
        return leftSum == rightSum

    if (arr[i] % 5 == 0):
        leftSum = leftSum + arr[i]
    elif (arr[i] % 3 == 0):
        rightSum = rightSum + arr[i]

    else:
        # NOT divisible by both 3 and 5
        # try both cases,
        ans1 = divideArrayIntoTwoHelper(arr, n, leftSum + arr[i], rightSum, i + 1)
        ans2 = divideArrayIntoTwoHelper(arr, n, leftSum, rightSum + arr[i], i + 1)
        return ans1 or ans2

        # For cases when element is multiple of 3 or 5.
    return divideArrayIntoTwoHelper(arr, n, leftSum, rightSum, i + 1)


def divideArrayIntoTwo(arr, n):
    # Initially start, lsum and rsum
    # will all be 0
    return divideArrayIntoTwoHelper(arr, len(arr), 0, 0, 0)


n = int(input())
arr = [int(i) for i in input().strip().split()]
print(divideArrayIntoTwo(arr, n))
