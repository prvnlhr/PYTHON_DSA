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
        if topEnd < start:
            stack.append(intervals[i])
        elif topEnd < end:
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
