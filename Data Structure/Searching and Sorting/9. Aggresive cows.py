# SEE STRIVER'S VIDEO FOR MORE DETAILED EXPLANATION
#
# Given stalls ::    [1, 2, 8, 4, 9]
# OK lets first understand the input stalls array
# At first pos , 0 index, we have stall no. 1
# At second pos, 1 index, we have stall no. 2
# At third pos , 2 index, we have stall no. 8
# At fourth pos, 3 index, we have stall no. 4
# At fifth pos , 4 index, we have stall no. 9

# Now we have given k == 3, that is 3 aggressive cows
# Now as these cows are aggressive , we cant put then side by side
# Given an array of length ‘N’, where each element denotes the
# position of a stall. Now you have ‘N’ stalls and an integer ‘K’
# which denotes the number of cows that are aggressive. To prevent
# the cows from hurting each other, you need to assign the cows to
# the stalls, such that the minimum distance between any two of them
# is as large as possible. Return the largest minimum distance.


def canPlace(stalls, dist, cows):
    lastCowPos = stalls[0]
    cowsCount = 1

    for i in range(1, len(stalls)):
        if stalls[i] - lastCowPos >= dist:
            cowsCount += 1
            lastCowPos = stalls[i]
            if cowsCount >= cows:
                return True
    return False


# OR_

def place(stalls, minDist, cows):
    lastCowPos = stalls[0]
    cowsCount = 1

    for i in range(1, len(arr)):
        currPos = arr[i]
        if currPos - lastCowPos >= minDist:
            cowsCount += 1
            lastCowPos = stalls[i]
            if cowsCount >= cows:
                return True
    return False


def aggressiveCows(stalls, cows):
    stalls.sort()
    n = len(stalls)
    lo = 0
    hi = arr[n - 1]  # we can take lo = 0 and hi = any large value,
    # so we took arr[n-1] because,
    # as stalls are sorted, arr[n-1] is largest.
    res = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if place(stalls, mid, cows):
            lo = mid + 1  # as we have to increase distance between cows , we increase lo if possible to place at currDist = mid
            res = mid
        else:
            hi = mid - 1
    return res


arr = [1, 2, 8, 4, 9]
cows = 3
ans = aggressiveCows(arr, cows)
print(ans)
