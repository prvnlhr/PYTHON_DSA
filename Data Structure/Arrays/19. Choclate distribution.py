# Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3
# Output: Minimum Difference is 2
# Explanation:
# We have seven packets of chocolates and
# we need to pick three packets for 3 students
# If we pick 2, 3 and 4, we get the minimum
# difference between maximum and minimum packet sizes.
#
# Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , m = 5
# Output: Minimum Difference is 6
# Explanation:
# The set goes like 3,4,7,9,9 and the output
# is 9-3 = 6
#
# Input : arr[] = {12, 4, 7, 9, 2, 23, 25, 41,
# 30, 40, 28, 42, 30, 44, 48,
# 43, 50} , m = 7
# Output: Minimum Difference is 10
# Explanation:
# We need to pick 7 packets. We pick 40, 41,
# 42, 44, 48, 43 and 50 to minimize difference
# between maximum and minimum.


def findMinDiff(arr, m):
    # if there are no chocolates or number of students is 0
    if m == 0 or len(arr) == 0:
        return 0
    arr.sort()
    print(arr)

    # Number of students cannot be more than number of packets
    if len(arr) < m:
        return -1
    # initially min_diff would be last and first element
    min_diff = arr[len(arr) - 1] - arr[0]

    for i in range(len(arr) - m + 1):
        # print(i, min_diff, arr[i], arr[i + m - 1], arr[i + m - 1] - arr[i])
        # update min_diff everytime
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])
    return min_diff


# arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
# m = 7
arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
ans = findMinDiff(arr, m)
print(ans)
