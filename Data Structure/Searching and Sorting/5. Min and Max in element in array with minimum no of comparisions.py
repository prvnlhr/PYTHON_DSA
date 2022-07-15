# WE HAVE TO FIND MIN AND MAX AND THE COMPARISONS ,
# DONE SHOULD BE MINIMUM
# Time Complexity: O(n)
#
# Total number of comparisons: Different for even and odd n, see below:
#
# If n is odd:    3 * (n-1)/2
# If n is even:   1 Initial comparison for initializing min and max,
#                 and 3(n-2)/2 comparisons for rest of the elements
#                 =  1 + 3*(n-2)/2 = 3n/2 -2


def minMax(arr):
    n = len(arr)

    if n % 2 == 0:  # 1 Comparison
        MIN = min(arr[0], arr[1])
        MAX = max(arr[0], arr[1])
        i = 2
    else:
        MIN, MAX = arr[0]
        i = 1

    while i < n - 1:
        if arr[i] < arr[i + 1]:  # comparison 1
            MIN = min(MIN, arr[i])  # comparison 2
            MAX = max(MAX, arr[i + 1])  # comparison 3
        else:
            MIN = min(MIN, arr[i + 1])
            MAX = max(MAX, arr[i])

        i += 2  # IMP

    return MIN, MAX


arr = [1000, 11, 445, 1, 330, 3000]
print(minMax(arr))
