# Leetcode
# Given an array of integers nums containing n + 1
# integers where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this
# repeated number.
#
# You must solve the problem without modifying the array
# nums and uses only constant extra space.

# nums = [1,3,4,2,2]
# output: 2

# SOL 1: sort the array. Repeating elements comes together
# Time O(NLogN) . Needs to modify the array by sorting

# SOL 2: Using map\set:
# Time O(n) and Space(n)

# SOL 3: Floyd's Tortoise and Hare (Cycle Detection)
# Time O(n) . space O(1)
#
#
# _SOL 1:______________________________________________________________
def findDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]


# _SOL 2:_________________________________________________________________
def findDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


# _SOL 3:__________________________________________________________________

# When we carefully observe Tortoise and Hare pointer, when dry running
# we found that hare pointer is running one step advance compare to tortoise
# How ??, well , tortoise = nums[tor],means it will take value at the index, and
# move to that place whereas, hare = mums[nums[hear]] , means it will take value
# as index and will move to that index value,


# Now What is purpose of Taking Tortoise and Hare.
#                          0  1  2  3  4
# On dry running for ex_ [ 1  3  4  2  2 ]
# We see at nums[nums[2]] = nums[4] = 2 , so at this step Hare pointer will stuck and Tortoise will also
# reach at Hare pointer and we will get our ans

def findDuplicate(nums):
    # Find the intersection point of the two runners.
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Find the "entrance" to the cycle.

    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare


nums = [int(i) for i in input().strip().split()]
ans = findDuplicate(nums)
print(ans)
