# Example 1:
#
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first
# two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:
#
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five
# elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def removeElement(nums, val):
    i = 0
    for curr_index in range(len(nums)):

        if nums[curr_index] != val:
            nums[i] = nums[curr_index]
            i += 1
    return i


# 1 2 3 4 5 2 2 6 7 8 2 9 10 2 3 2 2 2 2 23
# 2
# 1 3 4 5 6 7 8 9 10 3 23
nums = [int(i) for i in input().strip().split()]
val = int(input())
x = removeElement(nums, val)
for index in range(x):
    print(nums[index], end=' ')
