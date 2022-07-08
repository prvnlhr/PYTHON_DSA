import queue


# Input : arr[] = {-8, 2, 3, -6, 10}, k = 2
# Output : -8 0 -6 -6
# First negative integer for each window of size k
# {-8, 2} = -8
# {2, 3} = 0 (does not contain a negative integer)
# {3, -6} = -6
# {-6, 10} = -6
#
# Input : arr[] = {12, -1, -7, 8, -15, 30, 16, 28} , k = 3
# Output : -1 -1 -7 -15 -15 0

# _NAIVE APPROACH O(nk)
#
# _EFFICIENT APPROACH O(N):
# " Using queue and sliding window technique "

# Consider each sub-array of size k as a sliding window.
# Initialize two variables windowStart and windowEnd pointing
# to the first element of the array.
# These variables define the bounds of our sliding window.
# The initial window size is 1.
# Initialize a FIFO queue that stores the negative numbers
# in the current window in a First-in-First-Out order.
# Iterate over the array moving windowEnd forward by one element in each iteration.
# If the new element pointed by windowEnd is negative, then add it to the queue.
# If the window size hits to k (windowEnd-windowStart+1 == k), then
# Find the first negative number in the current window by getting the first
# element from the queue and store it in the result.
# If the queue is empty, that means the current window (current sub-array)
# did not have any negative number, so store 0 in the result.
# Now we need to slide the window ahead. So we need to discard the element at
# windowStart out of the window. To do this - Check if the first element
# in the queue is equal to the element at windowStart, if yes then remove it
# from the queue since it is going out of the window.
# Increment windowStart to slide the window ahead.

# arr = [12, -1, -7, 8, -15, 30, 16, 28]

#       s
#       |
#      [12, -1, -7, 8, -15, 30, 16, 28]   # if arr[e] -> -ve put it into queue
#       |                                   here we don't have -ve so move e further
#       e
#
#      s
#    [12, -1, -7, 8, -15, 30, 16, 28]  arr[e]-> -ve :: queue [-1] , e++
#          e
#
#      s
#     [12, -1, -7, 8, -15, 30, 16, 28]  arr[e]-> -ve :: queue [-1,-7]
#               e
#                                                now , e-s+1=k ,window hit
#                                                queue : [-1,-7]
#                                                so, num = queue[0] = -1  --> res.append(num)
#                                                res = [-1]
#                                                s++, e++
#
#           s
#     [12, -1, -7, 8, -15, 30, 16, 28]  ,  e-s+1=k, window hit ,
#                  e                       queue : [-1,-7]
#                                          so , num = queue[0] = -1 --> res.append(num)
#                                          now, num = queue[0] = arr[s]
#                                          so in next iteration window will move,
#                                          so -1 will be out of window, but
#                                          -1 is in queue, so we will need to
#                                          remove -1 from queue
#                                          s++, e++
#
#
#
#
#                   s
#         [12, -1, -7, 8, -15, 30, 16, 28] ,  e-s+1=k, window hit
#                           e                 queue : [-7,-15]
#                                             num = -7 --> res.append(num)
#                                             num = arr[s], so remove num from queue
#                                             queue = [-15]
#                                             s++, e++
# so above steps will repeat..........
def findFirstNegativeIndex(arr, k):
    q = queue.Queue()
    windowStart = 0
    result = []

    for windowEnd in range(len(arr)):

        if arr[windowEnd] < 0:
            q.put(arr[windowEnd])

        if windowEnd - windowStart + 1 == k:  # window size k hit
            if q.empty():
                result.append(0)
            else:
                num = q.queue[0]
                result.append(num)
                # if this condition is satisfied means we have queue top
                # ele at start of window, so we remove it so we didn't
                # take it again in next window
                if num == arr[windowStart]:
                    q.get()
            windowStart = windowStart + 1

    return result


arr = [int(i) for i in input().strip().split()]
k = int(input())

ans = findFirstNegativeIndex(arr, k)
print(ans)
