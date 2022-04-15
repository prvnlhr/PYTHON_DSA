# Given two non-negative integers low and high. Return the count
# of odd numbers between low and high (inclusive).
#
# Example 1:
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].


# Example 2:
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].
#


# APPROACH :
# if : low -> even , high -> even
#      then num of odd elements will be half the range (high -low) //2
# if : low -> odd , high -> even
#      then we need to make both even , so low = low-1
# if : low -> even , high -> odd
#      then we need to make both even , so high = high+1
# if : low -> odd , high -> odd
#       then (high-low)//2 + 1, one extra element

def countOdds(low, high):
    ans = None

    if (low % 2 == 0 and high % 2 == 0):
        ans = (high - low) // 2

    elif low % 2 == 0 and high % 2 != 0:
        high += 1
        ans = (high - low) // 2


    elif low % 2 != 0 and high % 2 == 0:
        low -= 1
        ans = (high - low) // 2


    elif low % 2 != 0 and high % 2 != 0:
        ans = ((high - low) // 2) + 1
    return ans

