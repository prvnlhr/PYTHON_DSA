# Given heights of n towers and a value k. We need to either
# increase or decrease the height of every tower by k (only once)
# where k > 0. The task is to minimize the difference between the
# heights of the longest and the shortest tower after modifications
# and output this difference.

# '''Minimize the maximum difference between the heights'''


# Examples:
#
# Input  : arr[] = {1, 15, 10}, k = 6
# Output :  Maximum difference is 5.
# Explanation : We change 1 to 7, 15 to
# 9 and 10 to 4. Maximum difference is 5
# (between 4 and 9). We can't get a lower
# difference.
#
# Input : arr[] = {1, 5, 15, 10}
#         k = 3
# Output : Maximum difference is 8
# arr[] = {4, 8, 12, 7}
#
# Input : arr[] = {4, 6}
#         k = 10
# Output : Maximum difference is 2
# arr[] = {14, 16} OR {-6, -4}
#
# Input : arr[] = {6, 10}
#         k = 3
# Output : Maximum difference is 2
# arr[] = {9, 7}
#
# Input : arr[] = {1, 10, 14, 14, 14, 15}
#         k = 6
# Output: Maximum difference is 5
# arr[] = {7, 4, 8, 8, 8, 9}
#
# Input : arr[] = {1, 2, 3}
#         k = 2
# Output: Maximum difference is 2
# arr[] = {3, 4, 5}


# APPROACH : REFER TECHIE'S CODE YT VIDEO

#  1  1  1  2  5  6  7  9  9  10
#                           a                           b
#                           |                           |
#                           1  1  1  2  5  6  7  9  9  10

# Consider the above case, Initially before making any changes to the array elements
# if the array is sorted what would be the max diff ??, Well if array is sorted maxEle(a) - minELe(b) = 10 - 1 = 9 is max Diff
# Now, as we have to minimise this diff , what could be the possible cases,
# 1. Increase a and b
# 2. Decrease a and b
# 3. Increase a, Decrease b
# 4. Decrease a, Increase b
# We first two cases would be absurd because, let say if a = 1, b = 10, diff = 10-1 = 9
# if both and b are increased -> a = a+1 , b = b+1 => a = 2 ,b = 11 , diff = 11 -2 = 9.
#
# Now, if we carefully observe, if we want to minimise the heights, we need to minimise the difference.
# So case 3. would be correct,to increase a and decrease b. So when we increase a and decrease b, we are reduce the distance between them
#
# Now again if we further look at the sorted array we find that, any two elements which are adjacent to each other
# will have minimum difference. i.e  arr[i-1] and arr[i].
# now if arr[i-1]{left ele} move towards right i.e arr[i-1]+k  and arr[i]{right ele} moves towards left i.e arr[i]-k , difference can be
# further decreased.
# Conclusion:
# Initially our minELe -> arr[0] , maxEle -> arr[n-1] , because arr is sorted.
# Further, to minimise diff ,we can do, minELe = arr[0]+k,  and maxELe = arr[n-1]-k , reducing the gap.
# Now, two adjacent elements are given as arr[i-1] and arr[i].
# If we want to reduce the gap between then, we can do -->  arr[i-1]+k  , arr[i]-k.
# So our minEle will be minimum of initial minELe i.e arr[0]+k and arr[i]-k
# and maxEle will be maximum of initial maxELe i.e arr[n-1]-k and arr[i-1]+k
#        MIN = min(arr[0] + k, arr[i] - k)
#        MAX = max(arr[n - 1] - k, arr[i - 1] + k)

# now diff = MAX-MIN
# and as we want to minimise the ans therefore, ans = min(ans, diff)
#  NOTE: there's a catch in the solution, as after subtracting k from element it should be non-negative(i.e remain positive),
#       so we cant subtract k from a element if it become negative.
#       if a element is equal or greater then k, then only we can subtract k from it, without making it negative,
#       else we need to skip that element


# Time Complexity: O(NlogN)
# Space Complexity: O(N)

def minimiseHeight(arr, n, k):
    arr.sort()

    ans = arr[n - 1] - arr[0]

    for i in range(1, n):
        if arr[i] >= k:  # if element is greater or equal to k then only do operation
            MIN = min(arr[0] + k, arr[i] - k)
            MAX = max(arr[n - 1] - k, arr[i - 1] + k)
            diff = MAX - MIN
            ans = min(ans, diff)
        else:  # skip element
            continue
    return ans


def getMinDiff(arr, n, k):
    if (n == 1):
        return 0

    arr.sort()

    ans = arr[n - 1] - arr[0]

    small = arr[0] + k
    big = arr[n - 1] - k

    if (small > big):
        small, big = big, small

    for i in range(1, n - 1):
        subtract = arr[i] - k
        add = arr[i] + k

        if subtract >= small or add <= big:
            continue

        if big - subtract <= add - small:
            small = subtract
        else:
            big = add

    return min(ans, big - small)


arr = [int(i) for i in input().strip().split()]
n = len(arr)
k = int(input())

ans = getMinDiff(arr, n, k)
print(ans)
