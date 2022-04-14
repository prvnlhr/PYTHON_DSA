# SELF SOLVED WITHOUT LOOKING,
# 1st attempt
# 100 % Correct


# O(N) ,O(1)___

# ITs kind of sliding window type approach
# APPROACH::
# i = 0 ,j = 0 , i ---> j , will be our window
# keep moving j and calculate currSum += arr[j]
# Now there are three conditions,
# if currSum == sum: we have our sub array from i to j
# elif currSum < sum: keep adding arr[j] and move j++
# elif currSum > sum : then window need to minimize ,and sum should
#                       so remove from window start , so currSum - arr[i] , i++


def subArray(arr, s):
    i = 0
    j = 0
    n = len(arr)
    currSum = 0
    while i < n and j < n:

        if currSum == s:
            return i, j


        elif currSum < s:
            currSum += arr[j]
            j += 1


        elif currSum > s:
            currSum -= arr[i]
            i += 1

    return -1


testCases = [[[1, 4, 20, 3, 10, 5], [33]], [[1, 4, 0, 0, 3, 10, 5], [7]],
             [[1, 4], [0]], [[15, 2, 4, 8, 9, 5, 10, 23], [23]]]
for arr, sum in testCases:
    ans = subArray(arr, sum[0])
    print(arr[ans[0]:ans[1]])
