# def maxSumSubArray(arr, size):
#     max = 0
#     sum = 0
#
#     for i in range(len(arr)):
#         sum = sum + arr[i]
#         if sum < 0:
#             sum = 0
#         elif (sum > max):
#             max = sum
#     return max
#

# works for all negative elements in array


# This is same as below solution, but here variable names are changed
# for better understanding
def maxSumSubArray(arr, size):
    max_sum = arr[0]
    max_sum_ending_here = arr[0]

    for i in range(1, size):
        # In below line , max_sum_ending_here will be sum calculated till that
        # array element. Now this calculated sum can be either increasing
        # or it may have decreased,if so then this can be our sub array,
        # so we take arr[i] as max_sum_ending_here because we will consider
        # new sub array from there
        max_sum_ending_here = max(arr[i], max_sum_ending_here + arr[i])
        max_sum = max(max_sum, max_sum_ending_here)
    return max_sum


# def maxSumSubArray(arr, size):
#     max_so_far = arr[0]
#     max_ending_here = arr[0]
#
#     for i in range(1, size):
#         max_ending_here = max(arr[i], max_ending_here + arr[i])
#         max_so_far = max(max_so_far, max_ending_here)
#     return max_so_far


# arr = [int(i) for i in input().strip().split()]
arr = [1, 2, -3, 4, 5, -2, 6, 5]
print(sum(arr))
ans = maxSumSubArray(arr, len(arr))
print(ans)
