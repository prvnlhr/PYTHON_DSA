def maxAreaOfHist(hist):
    stack = []
    currIndex = 0
    max_Area = 0
    # pseudo-code:

    # while 0 to len(hist):
    #     if (hist[currIndex] >= hist[stack[-1]])
    #       stack.append--> currIndex
    #       currIndex += 1
    #     else:
    #       stackTop = stack.pop()
    #       find the area = hist[stackTop] * currIndex
    #       max_Area = max(area,max_Area)

    # Again:
    # While stack:
    #     stackTop = stack.pop()
    #     find the area = hist[stackTop] * currIndex
    #     max_Area = max(area,max_Area)
    #
    # return max_Area






    
    while currIndex < len(hist):
        if (not stack) or hist[currIndex] >= hist[stack[-1]]:
            stack.append(currIndex)
            currIndex = currIndex + 1
        else:
            stackTop = stack.pop()
            if stack:
                area = hist[stackTop] * (currIndex - stack[-1] - 1)
            else:
                area = hist[stackTop] * currIndex
            max_Area = max(max_Area, area)

    while stack:
        stackTop = stack.pop()
        if stack:
            area = hist[stackTop] * (currIndex - stack[-1] - 1)
        else:
            area = hist[stackTop] * currIndex

        max_Area = max(max_Area, area)
    return max_Area


hist = [int(i) for i in input().strip().split()]
print(maxAreaOfHist(hist))
