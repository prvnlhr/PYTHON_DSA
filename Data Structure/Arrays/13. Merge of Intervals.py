# arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
# output = [1, 9]


# Time complexity : O(NlogN)
# Space complexity : O(NlogN) or O(N)

# STEPS:
# 1. Sort the array on basis of first element(start) of pair [[start,end],[start,end]]
# 2. Initialize stack with first element of array
# 3. for every element of input arr, there may be two conditions,
# ____if not overlapping --> since the array is sorted on basis of their start value, so to check
#                            overlapping we can compare curr element_start to stack_top_start,
#                            if stack_top start is smaller then no overlapping,hence append curr top stack

# ____if overlapping --> we do not check anything just change the stack top elements end with max(stack_top_end ,curr_end)


def mergeInterval(arr):
    # Sorting based on the increasing order
    # of the start intervals

    arr.sort(key=lambda x: x[0])
    stack = []
    # initialize stack with arr first element,
    stack.append(arr[0])

    for curr in arr:
        # for every element in arr,
        stack_top = stack[-1]
        stack_top_end = stack_top[1]
        curr_start = curr[0]

        # if this condition satisfies then there is no overlapping
        if stack_top_end < curr_start:
            stack.append(curr)

        # else there is overlapping just change
        # the stack top element and move for next iteration

        else:  # stack_top_end > curr_start :
            stack_top[1] = max(stack_top[1], curr[1])
    return stack


def merge(arr):
    arr.sort(key=lambda x: x[0])
    stack = []

    stack.append(arr[0])

    for i in range(1, len(arr)):
        if stack[-1][1] >= arr[i][0]:
            stack[-1][1] = max(stack[-1][1], arr[i][1])
        else:
            stack.append(arr[i])
    return stack


arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
# arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
(merge(arr))
print("ans1: ", mergeInterval(arr))
