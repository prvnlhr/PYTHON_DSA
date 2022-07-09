#
# Example 1:
# Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# Explanation: Since intervals[1, 3] and [2, 6] overlaps
# merge them into[1, 6].
#
# Example 2:
# Input: intervals = [[1, 4], [4, 5]]
# Output: [[1, 5]]
# Explanation: Intervals[1, 4] and [4, 5] are considered overlapping.

def mergeOverlappingIntervals(intervals):
    stack = []
    intervals.sort()
    stack.append(intervals[0])

    for i in range(1, len(intervals)):
        stackTop = stack[-1]
        start = intervals[i][0]
        end = intervals[i][1]
        topStart = stack[-1][0]
        topEnd = stack[-1][1]

        # always compare stackTop->END and curr->START
        if topEnd < start:
            stack.append(intervals[i])

        elif topEnd < end:
            # update stackTop->END to curr->END ,append it to stack
            stackTop[1] = end
            stack.pop()
            stack.append(stackTop)

    print(stack)


n = int(input())
intervals = []
for i in range(n):
    arr = [int(i) for i in input().strip().split()]
    intervals.append(arr)

mergeOverlappingIntervals(intervals)
