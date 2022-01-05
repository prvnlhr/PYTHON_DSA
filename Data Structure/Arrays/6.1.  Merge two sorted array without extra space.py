# arr1 = [1,3,5,7]
# arr2 = [0,2,6,8,9]

# output:
# 0 1 2 3
# 5 6 7 8 9

# Input: ar1[] = {1, 5, 9, 10, 15, 20};
#        ar2[] = {2, 3, 8, 13};
# Output: ar1[] = {1, 2, 3, 5, 8, 9}
#         ar2[] = {10, 13, 15, 20}

# The idea is: We will traverse the first array and compare it with the first element of the second array.
# If the first element of the second array is smaller than the first array then we will swap and then
# sort the second array. First, we have to traverse array1 and then compare it with the first element of array2.
# If it is less than array1 then swap we swap both.
#
# After swapping we are going to sort the array2 again so that the smallest element of the array2
# comes at the first position and we can again swap with the array1
# To sort the array2 we will store the first element of array2 in a variable and left shift all the element and store
# the first element in array2 in the last.

def mergeTwoSortedArray(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    # step1: traverse arr1 and compare first element of arr2. If arr2 first element is less
    # then arr1 element swap
    for i in range(n):
        print("arr1:", arr1)
        print("arr2", arr2)
        print("comparing :", arr1[i], arr2[0])
        if (arr1[i] > arr2[0]):
            arr1[i], arr2[0] = arr2[0], arr1[i]
            print("after comparing swapping :")
            print(arr1)
            print(arr2)
            print()

            # step2: after swapping , we have to sort the array2 again so that it
            # can be again swap with arr1
            # we will store the firstElement of array2
            # and left shift all the element and store
            # the firstElement in arr2[k-1]
            arr2.sort()
            # firstEle = arr2[0]
            # k = 1
            # while k < m and arr2[k] < firstEle:
            #     arr2[k - 1] = arr2[k]
            #     k = k + 1
            # arr2[k - 1] = firstEle
            # print("after sorting arr2 :")
            # print(arr2)
            # print()

    return arr1, arr2


arr1 = [int(i) for i in input().strip().split()]
arr2 = [int(j) for j in input().strip().split()]

ans = mergeTwoSortedArray(arr1, arr2)
print(ans)
