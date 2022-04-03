#
# Inversion Count for an array indicates – how far (or close) the array is from being sorted.
# If the array is already sorted, then the inversion count is 0, but if the array is sorted
# in the reverse order,the inversion count is the maximum.
# Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
#
# Input: arr[] = {8, 4, 2, 1}
# Output: 6
#
# Explanation: Given array has six inversions:
# (8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).
#
#
# Input: arr[] = {3, 1, 2}
# Output: 2
#
# Explanation: Given array has two inversions:
# (3, 1), (3, 2)


# APPROACH ::
# a[i] > a[j] and i < j

# [ 8, 4, 2, 1 ]

# i = 0 , -> 8
#    from  j = i+1 ->n ->  4 , 2 , 1
#  now as arr[i] > arr[j] ,they can make pairs as (8,4) (8,2) (8,1)
# Similarly, for i=1 -> 4 -> (4,2) (4,1)
# i=2 -> 2 -> (2,1)
# Therefore 6 pairs(inversion)

# Naive Solution___ O(n^2)

# def countInversion(arr):
#     inv_count = 0
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:
#                 inv_count = inv_count + 1
#


# _____________________________________________________

# Now to optimise it from O(n*n) to N logN,
# we can use merge sort technique
# Because in merge sort , in merge process, we always compare
# the elements using pointer i,j , if arr[i] > arr[j] , then we have a pair.


# MergeSort Technique__O(n log n)

def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return 0
    inv_count = 0
    mid = len(arr) // 2
    a1 = arr[0:mid]
    a2 = arr[mid:]
    inv_count += merge_sort(a1)
    inv_count += merge_sort(a2)
    inv_count += merge(a1, a2, arr)
    return inv_count


# SEE STRIVER'S YT VIDEO
def merge(a1, a2, arr):
    i = 0
    j = 0
    k = 0
    count = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            i = i + 1
            k = k + 1


        # this is the condition of inversion pair,
        elif a1[i] > a2[j]:
            arr[k] = a2[j]

            # Main trick__
            # In merge process, let i is used for indexing left sub-array and
            # j for right sub-array. At any step in merge(), if a[i] is greater
            # than a[j], then there are (mid – i) inversions, because left and
            # right sub-arrays are sorted, so all the remaining elements in
            # left sub-array (a[i+1], a[i+2] … a[mid]) will be greater than a[j]

            # Ex_ [7, 9, 11,]      [ 3, 4, 5 ]
            #
            #         i = 0 -> 7, j = 0,  if 7 > 3,  then all elements from 7 onwards in left array
            #                                        will be greater then 3, so 7 will have to move
            #                                        5 places to left i.e  len(a1)-i.
            #                                        So count will be count = count + (n - i)

            count = count + (len(a1) - i)

            j = j + 1
            k = k + 1

    while i < len(a1):
        arr[k] = a1[i]
        k = k + 1
        i = i + 1
    while j < len(a2):
        arr[k] = a2[j]
        k = k + 1
        j = j + 1

    return count


# arr = [int(i) for i in input().strip().split()]
arr = [1, 2, 6, 7, 8, 9, 3, 4, 5]
ans = merge_sort(arr)
print(ans)
