#
#
# SEE ADITYA VERMA STACK PLAYLIST FOR BETTER UNDERSTANDING
#
# NEAREST SMALLEST TO LEFT OR NEXT SMALLER TO LEFT
def NSL(arr):
    stack = []
    res = [-1] * len(arr)
    res[0] = -1
    stack.append(arr[0])

    for i in range(1, len(arr)):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            res[i] = (stack[-1])
        else:
            res[i] = -1
        stack.append(arr[i])
    return res


testCases = [[1, 6, 4, 10, 2, 5], [1, 3, 0, 2, 5], [4, 2, 1, 5, 6, 3, 2, 4, 2]]
for test in testCases:
    ans = NSL(test)
    print(ans)
