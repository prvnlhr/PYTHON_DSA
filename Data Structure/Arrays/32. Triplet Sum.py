from sys import stdin


# Naive O(n^3)
def findTriplet(arr, n, x):
    paircount = 0
    for i in range(n):
        for j in range((i + 1), n):
            for k in range((j + 1), n):
                if (arr[i] + arr[j] + arr[k] == x):
                    paircount = paircount + 1
    print(paircount)


# OPTIMISED O(n^2) , O(1)
# Complexity Analysis:
# Time complexity: O(N^2).
# There are only two nested loops traversing the array,
# so time complexity is O(n^2). Two pointers algorithm
# takes O(n) time and the first element can be fixed using
# another nested traversal.
# Space Complexity: O(1). As no extra space is required.

def tripletSum(arr, SUM):
    n = len(arr)
    arr.sort()

    for num1Index in range(n - 2):
        num2Index = num1Index + 1
        num3Index = n - 1
        while num2Index < num3Index:
            if arr[num1Index] + arr[num2Index] + arr[num3Index] == SUM:
                print(arr[num1Index], arr[num2Index], arr[num3Index])
                return
                # num1Index += 1
                # num3Index -= 1
            elif arr[num1Index] + arr[num2Index] + arr[num3Index] < SUM:
                num2Index += 1
            elif arr[num1Index] + arr[num2Index] + arr[num3Index] > SUM:
                num3Index -= 1


testCases = [[[12, 3, 4, 1, 6, 9], [24]], [[1, 4, 45, 6, 10, 8], [22]], [[1, 2, 3, 4, 5], [9]]]
for test in testCases:
    arr = test[0]
    sum = test[1][0]
    tripletSum(arr, sum)
