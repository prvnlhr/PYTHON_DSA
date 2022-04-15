# T: O(n) , S:O(1)
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first 3
# five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# LEETCODE SPECIFIC OUTPUT, REMOVING DUPLICATES
def removeDuplicates(nums):
    n = len(nums)
    if n == 0 or n == 1:
        return n
    j = 0

    for i in range(0, n - 1):
        if nums[i] != nums[i + 1]:
            nums[j] = nums[i]
            j = j + 1
    # for end element because above we are running loop till second last element only so,

    nums[j] = nums[n - 1]
    j = j + 1
    return j


# GENERIC SOLUTION O(logN), TO FIND IN SORTED ARRAY
# BINARY SEARCH SOLUTION


def findDUPSINsorted(arr):
    res = []

    def find(lo, hi):
        if lo > hi:
            return -1
        mid = (lo + hi) // 2

        if arr[mid] != arr[mid + 1]:

            if mid > 0 and arr[mid] == arr[mid - 1]:
                return res.append(mid)

            return find(lo, mid - 1)

        return find(mid + 1, hi)

    find(0, len(arr) - 1)
    return res


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# n = (removeDuplicates(arr))
ans = findDUPSINsorted(arr)

for i in range(n):
    print(arr[i])
