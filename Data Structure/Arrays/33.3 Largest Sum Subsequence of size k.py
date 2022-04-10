# Input: arr[] = {-1, 3, 4, 2, 5}, K = 3
# Output: 3 4 5
# Explanation: Subsequence 3 4 5 with sum 12 is the subsequence with maximum possible sum.
#
#
# Input: arr[] = {6, 3, 4, 1, 1, 8, 7, -4, 2}
# k = 4
# Output: 6 3 4 8 7


# APPROACH :
# if we want to find max Sum subsequence of size k
# then if we look carefully then the result we contain
# all the largest k elements.

# Ex. [6, 3, 4, 1, 1, 8, 7, -4, 2] , k = 5
# res ->   8 7 6 4 3 -> all max k  elements from array
# So our problem boils down to finding k max elements from array
# Now there's a catch that even if we found k max elements their order
# should be exactly same as input array, so to form the correct subarray
# like  8 7 6 4 3  -> in input array there are in order like -> 6 3 4 8 7.

# So we can use a extra array to store a pair of (element,index)
# so that in final res we can get them in order of index.


# T : O(NlogN)
def maxSumSub(arr, k):
    ans = []
    n = len(arr)
    for i in range(n):
        ans.append([arr[i], i])

    ans.sort(key=lambda x: x[0])
    res = []

    for i in range(n - 1, n - k - 1, -1):
        res.append(ans[i][1])
    res.sort()

    for i in range(len(res)):
        res[i] = arr[res[i]]
    return res


arr = [6, 3, 4, 1, 1, 8, 7, -4, 2]
k = 5
print(maxSumSub(arr, k))
