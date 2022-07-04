#
import queue
from collections import deque



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


arr = [2, 5, -1, 7, -3, -1, -2]

# arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 4

ans = maxInWindow(arr, k)
print(ans)
