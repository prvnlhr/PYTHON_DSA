#
# Given an array and a range [lowVal, highVal], partition the array
# around the range such that array is divided in three parts.
# 1) All elements smaller than lowVal come first.
# 2) All elements in range lowVal to highVVal come next.
# 3) All elements greater than highVVal appear in the end.
# The individual elements of three sets can appear in any order.
#
# Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}
#         lowVal = 14, highVal = 20
# Output: arr[] = {1, 5, 4, 2, 1, 3, 14, 20, 20, 98, 87, 32, 54}
#
# Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}
#        lowVal = 20, highVal = 20
# Output: arr[] = {1, 14, 5, 4, 2, 1, 3, 20, 20, 98, 87, 32, 54}


#
# Simple solution will be to sort array using merge sort O(NlogN)
#
# Efficient solution using two pointer
# Time Complexity: O(n)
# Auxiliary Space: O(1)


def threeWayPartition(arr, low, high):
    curr_low_index = 0
    curr_high_index = len(arr) - 1
    i = 0
    while i < curr_high_index:

        # if element is smaller then low, swap with curr_low_index and increment i and curr_low_index
        if arr[i] < low:
            arr[i], arr[curr_low_index] = arr[curr_low_index], arr[i]
            i = i + 1
            curr_low_index = curr_low_index + 1
        # if curr ele is larger then high, swap with curr_high_index and decrement curr_high_index
        elif arr[i] > high:
            arr[i], arr[curr_high_index] = arr[curr_high_index], arr[i]
            curr_high_index = curr_high_index - 1
        # else element is in range low to high, increment i
        else:
            i = i + 1
    return arr


arr = [int(i) for i in input().strip().split()]
range = [int(j) for j in input().strip().split()]
ans = threeWayPartition(arr, range[0], range[1])
print(ans)
