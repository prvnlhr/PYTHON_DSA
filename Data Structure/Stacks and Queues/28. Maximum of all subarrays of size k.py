# Given an array and an integer K, find the maximum for
# each and every contiguous sub-array of size k.
#
# Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3
# Output: 3 3 4 5 5 5 6
# Explanation:
# Maximum of 1, 2, 3 is 3
# Maximum of 2, 3, 1 is 3
# Maximum of 3, 1, 4 is 4
# Maximum of 1, 4, 5 is 5
# Maximum of 4, 5, 2 is 5
# Maximum of 5, 2, 3 is 5
# Maximum of 2, 3, 6 is 6
#
# Input: arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}, K = 4
# Output: 10 10 10 15 15 90 90
# Explanation:
# Maximum of first 4 elements is 10, similarly for next 4
# elements (i.e from index 1 to 4) is 10, So the sequence
# generated is 10 10 10 15 15 90 90
from collections import deque


#
# INTUITION::
# arr = [1, 2, 3, 1, 4, 5, 2, 3, 6], K = 3
# Consider the above example,
# To solve this problem, first we will need some basic
# questions to be answered.
# 1. How many sub arrays of size k exists in input array
# 2. And finally what technique
# 3. What data structure we will need to solve this problem
# Well answers are...__________
# 1. For arr of size n , total subarray of size k will be given as , (n - k +1)
# 2. Well as this questions has subarray of size k init ,we can use sliding windows technique
# 3. As we are using sliding window approach,
#  we will need to maintain all the maximum from subarray of size k,
# so we can use a queue ,but here we will use two way queue ,Deque.
# Now what is Dequeue ,used for here?? the answer is the intuition we are using here
#
# Well for every window of size k we will put the element in queue if it is larger then ele in queue
# so at queue[-1] we will have a max ele
# now let say we move our windows ,so at some time the element in the queue will be out of window ele,so we need
# to remove them in queue,so we used dequeue,so that we can popleft() to delete ele from left of queue top ,
# if ele is out of curr window.
# now whenever we get a window size we will have our ans at queue[0].
def maximumofAll(arr, k):
    n = len(arr)

    Q = deque()  # Dequeue for two way popping elements

    res = [-1] * (n - k + 1)  # maintaining res for all sub-array of size k
    res_index = 0  # index for storing res in res array

    # NOTE:: we are putting index i to queue to not actual value
    for i in range(n):  # for ele in arr loop

        # 1. if ele in queue is out of curr window ,just pop it
        if Q and Q[0] <= i - k:
            Q.popleft()

        # 2. if ele in queue is smaller then curr arr[i] ,just pop it
        while Q and arr[Q[-1]] <= arr[i]:
            Q.pop()
        # else put it in queue
        Q.append(i)

        # if we reached our window size we will have our ele at Q[0]
        if i >= k - 1:
            res[res_index] = arr[Q[0]]
            res_index += 1

    return res


# SELF SOLVED 100% LEETCODE
# MORE SIMILAR TO NEGATIVE IN WINDOW OF SIZE K.
# MORE GENERIC SOLUTION
# MADE MORE EASY
def maxInWindow(arr, k):
    n = len(arr)
    q = deque()
    res = []
    winEnd = 0
    winStart = 0

    while winEnd < n:

        curr = arr[winEnd]  # curr ele of arr

        while q and q[-1] < curr:  # remove all q elements which are smaller then curr
            q.pop()
        q.append(curr)  # and append curr

        if winEnd - winStart + 1 == k:  # if window hit

            if q:  # and if q is not empty
                res.append(q[0])  # then append q top to res
                if q[0] == arr[winStart]:  # and if q top  is out of window remove
                    q.popleft()
            else:  # else if q is empty
                res.append(0)  # then append 0 to res
            winStart += 1  # finally moving window

        winEnd += 1
    return res


testCases = [[[8, 5, 10, 7, 9, 4, 15, 12, 90, 13], [4]], [[1, 2, 3, 1, 4, 5, 2, 3, 6], [3]],
             [[12, 1, 78, 90, 57, 89, 56], [3]]]

for test in testCases:
    arr = test[0]
    k = test[1][0]
    ans = maximumofAll(arr, k)
    print(ans)
