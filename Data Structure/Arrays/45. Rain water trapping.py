# Time complexity: O(n).

# Space complexity: O(n) extra space.
# Additional O(n) space for left and right arrays .


# https://leetcode.com/problems/trapping-rain-water/
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by
# array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.

#            '''ANUJ YT VIDEO'''
# THIS IS DP BASED SOLUTION, BECAUSE WE ARE PREPROCESSING THE INPUT ARRAY
# TO STORE OUR ANS IN LEFT AND RIGHT ARRAYS
#
def trappingWater(arr):
    n = len(arr)
    left = [0] * n
    right = [0] * n

    maxLeft = arr[0]
    for i in range(n):
        maxLeft = max(maxLeft, arr[i])
        left[i] = max(maxLeft, arr[i])

    print(left)
    maxRight = arr[-1]

    for j in range(n - 1, -1, -1):
        maxRight = max(maxRight, arr[j])
        right[j] = max(maxRight, arr[j])
    print(right)

    maxUnitWater = 0

    for index in range(n):
        waterAtIndex = min(left[index], right[index])
        heightAtIndex = arr[index]
        maxUnitWater += waterAtIndex - heightAtIndex
    return maxUnitWater


# arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
arr = [3, 0, 2, 0, 4]
# arr = [2, 0, 2]
ans = trappingWater(arr)
print(ans)
