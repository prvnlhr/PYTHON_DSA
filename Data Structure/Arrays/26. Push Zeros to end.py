# Given an array of n numbers. The problem is to move
# all the 0’s to the end of the array while maintaining
# the order of the other elements. Only single traversal
# of the array is required
#
# Input : arr[]  = {1, 2, 0, 0, 0, 3, 6}
# Output : 1 2 3 6 0 0 0
#
# Input: arr[] = {0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9}
# Output: 1 9 8 4 2 7 6 9 0 0 0 0 0
#

# NAIVE:::
def pushZerosToEnd1(arr):
    n = len(arr)
    for i in range(n):
        print("i", i)
        if (arr[i] == 0):
            for j in range(i + 1, n):
                if (arr[j] != 0):
                    arr[i], arr[j] = arr[j], arr[i]
                    break
                    print(arr)


# OPTIMISED O(N)
def pushZeroesToEnd(arr):
    i = 0
    for curr_index in range(len(arr)):
        if arr[curr_index] != 0:
            arr[i] = arr[curr_index]
            i = i + 1
    # the upper loop will move all non zero to forward

    # now from i --> end make all elements as zero
    for j in range(i, len(arr)):
        arr[j] = 0


arr = [int(i) for i in input().split()]

pushZeroesToEnd(arr)
print(arr)
