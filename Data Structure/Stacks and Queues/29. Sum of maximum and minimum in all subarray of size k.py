from collections import deque


# Given an array of both positive and negative integers,
# the task is to compute sum of minimum and maximum elements
# of all sub-array of size k.

# Input : arr[] = {2, 5, -1, 7, -3, -1, -2}
#         K = 4
# Output : 18
# Explanation : Subarrays of size 4 are :
#      {2, 5, -1, 7},   min + max = -1 + 7 = 6
#      {5, -1, 7, -3},  min + max = -3 + 7 = 4
#      {-1, 7, -3, -1}, min + max = -3 + 7 = 4
#      {7, -3, -1, -2}, min + max = -3 + 7 = 4
#      Sum of all min & max = 6 + 4 + 4 + 4
#                           = 18
def sumMinMax(arr, k):
    n = len(arr)
    # As we required both min and max, we will maintain
    # two deque for min and max elements index
    minQ = deque()
    maxQ = deque()

    # Sum will store our ans
    sum = 0

    for i in range(n):

        # # 1.a if ele in minQ  is out of curr window, just pop it
        if minQ and minQ[0] <= i - k:
            minQ.popleft()

        # 1.b if ele in maxQ is out of curr window, just pop it
        if maxQ and maxQ[0] <= i - k:
            maxQ.popleft()

        # 2.a if ele in minQ is greater then curr arr[i] ,just pop it
        while minQ and arr[minQ[-1]] >= arr[i]:
            minQ.pop()

        # 2.b if ele in maxQ is smaller then curr arr[i] ,just pop it
        while maxQ and arr[maxQ[-1]] <= arr[i]:
            maxQ.pop()

        # else put it in queue
        minQ.append(i)
        maxQ.append(i)

        # if we reached our window size we will have our ele
        # index at minQ[0] and maxQ[0], so find sum
        if i >= k - 1:
            minCurr = arr[minQ[0]]
            maxCurr = arr[maxQ[0]]
            x = minCurr + maxCurr
            sum += x

    # return calculated sum
    return sum


# More generic same as other solutions of sliding window
def maxInWindow(arr, k):
    n = len(arr)
    maxQ = deque()
    minQ = deque()
    res = []
    winEnd = 0
    winStart = 0

    while winEnd < n:
        curr = arr[winEnd]

        while minQ and minQ[-1] > curr:
            minQ.pop()
        while maxQ and maxQ[-1] < curr:
            maxQ.pop()
        minQ.append(curr)
        maxQ.append(curr)

        if winEnd - winStart + 1 == k:

            if minQ and maxQ:
                res.append(minQ[0] + maxQ[0])

                if minQ[0] == arr[winStart]:
                    minQ.popleft()
                if maxQ[0] == arr[winStart]:
                    maxQ.popleft()
            else:
                res.append(0)
            winStart += 1

        winEnd += 1

    return res


testCases = [[[2, 5, -1, 7, -3, -1, -2], [4]], [[2, 5, -1, 7, -3, -1, -2], [3]], [[1, 2, 3, 4, 5], [3]],
             [[2, 4, 7, 3, 8, 1], [4]]]
for test in testCases:
    arr = test[0]
    k = test[1][0]
    ans = sumMinMax(arr, k)
    print(ans)
