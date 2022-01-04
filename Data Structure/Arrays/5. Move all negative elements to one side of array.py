# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -6  -13  -5  -3 -7  5   6  11

# IN this solution order of element is not maintained,just
# negatives are brought to one side . Another solution exists
# which maintains the array order, which is hard solution.
#
# Two pointer approach , T: O(N) , S: O(1)

def movePositiveToEnd(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:

        if (arr[i] < 0 and arr[j] < 0):  # both value are negative
            i = i + 1

        elif (arr[i] > 0 and arr[j] < 0):  # positive and negative
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            j = j - 1

        elif (arr[i] > 0 and arr[j] > 0):  # both values are positive
            j = j - 1

        elif (arr[i] < 0 and arr[j] > 0):  # negative and positive
            i = i + 1
            j = j - 1
    return arr


arr = [int(i) for i in input().strip().split()]

ans = movePositiveToEnd(arr)
print(ans)
