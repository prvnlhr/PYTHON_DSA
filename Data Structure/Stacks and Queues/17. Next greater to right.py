# Given an array, print the Next Greater Element (NGE)
# for every element. The Next greater Element for an
# element x is the first greater element on the right
# side of x in the array. Elements for which no greater
# element exist, consider the next greater element as -1.

# [4, 5, 2, 25],
#
# Element       NGE
#    4      -->   5
#    5      -->   25
#    2      -->   25
#    25     -->   -1
#
# [13, 7, 6, 12]
# Element     NGE
# 13 -->    -1
# 7 -->     12
# 6 -->     12
# 12 -->     -1


# LEETCODE SOLUTION O(N) O(N) OPTIMIZE
def nextGreater(arr):
    stack = []
    n = len(arr)
    ans = [-1 for i in range(n)]

    # STEPS ::
    # append a arr[i] to stack,
    # for every element in array --> arr[i], check if it stackTop is smaller then arr[i]
    # if stackTop is smaller pop it till stackTop becomes greater
    # now, if stack doesnt not becomes empty after popping means,we have a greater element in stack ,
    # so we will place it in ans array.

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(arr[i])
    return ans


def findNextGreater(arr):
    stack = []
    ans = []
    stack.append(-1)
    # ans.append(-1)
    ans = [None] * len(arr)

    curr = len(arr) - 2

    ans[len(arr) - 1] = -1

    # traverse the array starting from 2nd last element
    while curr >= 0:
        # if curr element of array is smaller then curr + 1 ,
        # we have ans for this element, append it to ans array
        if arr[curr] < arr[curr + 1]:
            # ans.append(arr[curr + 1])
            ans[curr] = arr[curr + 1]
            # also check if element appended ans array is also
            # greater then stack top element,then append it to stack
            if arr[curr + 1] > stack[-1]:
                stack.append(arr[curr + 1])
        else:

            stackTop = stack[-1]
            ansTop = ans[curr + 1]
            # print(arr[curr], stackTop, ansTop)

            if ansTop > arr[curr]:
                ans[curr] = ansTop

            elif stackTop > arr[curr]:
                # ans.append(stack[-1])
                ans[curr] = stackTop
            else:
                # ans.append(-1)
                ans[curr] = -1
                stack.append(arr[curr])
        curr = curr - 1
    print(stack)
    return ans


arr = [int(i) for i in input().strip().split()]

# ans = nextGreater(arr)
ans = nextGre(arr)
print(ans)
