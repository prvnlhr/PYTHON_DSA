import sys

MIN_VALUE = -2147483648


# Given an array of integers, our task is to write
# a program that efficiently finds the second largest
# element present in the array.
# Input: arr[] = {12, 35, 1, 10, 34, 1}
# Output: The second largest element is 34.
# Explanation: The largest element of the
# array is 35 and the second
# largest element is 34
#
# Input: arr[] = {10, 5, 10}
# Output: The second largest element is 5.
# Explanation: The largest element of
# the array is 10 and the second
# largest element is 5
#
# Input: arr[] = {10, 10, 10}
# Output: The second largest does not exist.
# Explanation: Largest element of the array
# is 10 there is no second largest element

def scondL(arr, n):
    lar = -sys.maxsize
    secondL = -sys.maxsize

    for i in range(n):
        if arr[i] > lar:
            secondL = lar
            lar = arr[i]
        if arr[i] > secondL and arr[i] < lar and arr[i] != lar:
            secondL = arr[i]
    return secondL


def secondLargest(arr, n):
    if (n == 0):
        return MIN_VALUE
    largest = arr[0]
    secondLargest = MIN_VALUE
    print(sys.maxsize)
    print(~(sys.maxsize))

    for i in range(n):
        if (arr[i] > largest):
            secondLargest = largest
            largest = arr[i]
        if (arr[i] > secondLargest and arr[i] != largest):
            secondLargest = arr[i]
    return secondLargest


n = int(input())
arr = [int(i) for i in input().split()]
# ans = secondLargest(arr, n)
ans = scondL(arr, n)
print(ans)
