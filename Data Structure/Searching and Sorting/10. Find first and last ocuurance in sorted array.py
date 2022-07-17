# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
#
# Input: nums = [], target = 0
# Output: [-1,-1]


# helper 1
def findStartingIndex(nums, target):
    index = -1  # 5
    low, high = 0, len(nums) - 1  # 6

    while low <= high:  # 7
        mid = low + (high - low) / 2  # 8

        if nums[mid] == target:  # 9
            index = mid  # 10
            high = mid - 1  # 11
        elif nums[mid] > target:  # 12
            high = mid - 1  # 13
        else:  # 14
            low = mid + 1  # 15

    return index


def findEndingIndex(nums, target):
    index = -1
    low, high = 0, len(nums) - 1

    while low <= high:

        mid = low + (high - low) / 2

        if nums[mid] == target:
            index = mid
            low = mid + 1  # 16
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return index


def searchRange(nums, target):
    result = [-1, -1]  # 1

    result[0] = findStartingIndex(nums, target)  # 2
    result[1] = findEndingIndex(nums, target)  # 3

    return result  # 4


# Here two helper functions are exactly the same except for one line (there are ways to actually combine the two,
# but, I though it's much easier to read and understand this way). The only difference is between line #11 and
# line #16 because the findStartingIndex would try to find the starting value and need to go to the left most
# target value in the array. However, findEndingIndex would try to find the right most one. So, in the first
# helper function, we try to narrow the limit of search (by changing low and high. We make high = mid - 1 in line #11)
# to focus on the left side of mid while we do the same for right side in the second helper function
# (low = mid + 1, line #16), does this make sense? Good. From now on, I'll focus on the findStartingIndex function.


arr = [5, 7, 7, 8, 8, 10]
target = 8
ans = searchRange(arr, target)
print(ans)
