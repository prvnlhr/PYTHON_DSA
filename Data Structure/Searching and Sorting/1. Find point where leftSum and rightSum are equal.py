# FIND POINT WHERE SUM OF LEFT ELEMENTS IS EQUAL TO SUM OF RIGHT ELEMENTS


def findPivot1(arr):
    SUM = sum(arr)
    RHTSUM = 0
    for i in range(len(arr) - 1, -1, -1):
        RHTSUM += arr[i]
        LFTSUM = SUM - RHTSUM + arr[i]
        if LFTSUM == RHTSUM:
            return i
    return -1


def findLSequalRs(arr):
    SUM = sum(arr)
    LFTSUM = 0

    for i in range(len(arr)):
        RHTSUM = SUM - LFTSUM - arr[i]
        if LFTSUM == RHTSUM:
            return i
        LFTSUM += arr[i]
    return -1


# LEETCODE::
# O(N),O(1)
def findPivot(arr):
    SUM = sum(arr)
    LFTSUM = 0
    n = len(arr)
    for i in range(n):
        LFTSUM = LFTSUM + arr[i]
        currLFTSUM = LFTSUM - arr[i]
        currRHTSUM = SUM - LFTSUM
        if currLFTSUM == currRHTSUM:
            return i
    return -1


arr = [1, 7, 3, 6, 5, 6]
# arr = [-1, -1, 0, 0, -1, -1]
ans1 = findPivot(arr)
ans2 = findPivot(arr)
ans3 = findLSequalRs(arr)
print(ans1, ans2, ans3)
