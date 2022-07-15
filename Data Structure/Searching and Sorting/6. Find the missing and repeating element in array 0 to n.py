from collections import defaultdict


# find missing and repeating number from arr of 1 to n integers
# Ex_ [4, 3, 6, 2, 1, 1]

def findMissingAndRepeating(arr):
    map = set()
    repeating = None
    missing = None
    n = len(arr)

    for ele in arr:
        if ele not in map:
            map.add(ele)
        else:
            repeating = ele

    # Now, if there are 1 to n elements in array.
    # for ex [4, 3, 6, 2, 1, 1]
    # So in map we would have, { 1, 2, 3, 4, 5}
    # now if we run a loop from 1 to n + 1 --> i.e  1, 2, 3, 4, 5, 6
    # if any of index is not found in  map ,means that is missing number
    for index in range(1, n + 1):
        if index not in map:
            missing = index
    return missing, repeating


arr = [4, 3, 6, 2, 1, 1]
# arr = [1, 1, 3, 4, 5, 6]

# arr = [2, 2]
ans = findMissingAndRepeating(arr)
print(ans)
