#
# EX__. [6 3 -1 -3 4 -2 2 4 6 -12 -7]

# subarray from 2 to 4
# subarray from 2 to 6
# subarray from 5 to 6
# subarray from 6 to 9
# subarray from 0 to 10

# map = {
# 6: [0],
# 9: [1, 4, 6],
# 8: [2], 5: [3],
# 7: [5, 9],
# 13: [7],
# 19: [8],
# 0: [10]
# }


# INTUITION:
# 1. Traverse a array and find sum at that point
# 2. Check if sum is in map or not
# 3. if not in map ,then append the sum to map and index of that sum
# 4. if sum in map , get [index array] at that sum from map, and iterate over it
# See gfg dry run image for better understanding

# OPTIMIZED__using map
from collections import defaultdict


def subArray(arr):
    map = defaultdict(list)
    output = []
    sum = 0

    for i, ele in enumerate(arr):

        sum += ele

        # if sum == 0 :  array from start to i is subarray
        if sum == 0:
            output.append((0, i))

        if sum in map:  # if sum in map
            subarray = map[sum]
            for x in subarray:
                val = x + 1
                output.append((val, i))

            # after printing append current i to subarray
            subarray.append(i)
            map[sum] = subarray

        elif sum not in map:
            map[sum] = [i]

    print(output)


def subArraySumToZero(arr):
    map = {}
    output = []
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]  # find sum up to curr index

        if sum == 0:
            output.append((0, i))

        al = []
        if sum in map:  # if sum is already in map
            al = map[sum]  # get sum val from map
            # iterate over sum value obtained from map , sum : [ . . . . ]
            for j in range(len(al)):  # sum : [ . . . ]
                # j + 1 index gives  start of sub-array with sum  j+1 --> i is required sub-array
                output.append((al[j] + 1, i))  # append it to output

        al.append(i)  # append curr index to al and put it into map
        map[sum] = al
    return output


arr = [6, 3, - 1, - 3, 4, - 2, 2, 4, 6, - 12, - 7]
# ans = subArraySumToZero(arr)
ans = subArray(arr)
print(ans)
# for x in ans:
# print('subarray from', x[0], 'to', x[1])
