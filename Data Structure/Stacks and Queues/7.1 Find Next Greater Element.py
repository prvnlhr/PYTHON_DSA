def findNextGreater(arr):
    stack = []
    ans = []
    stack.append(-1)
    # ans.append(-1)
    ans = [None] * len(arr)

    curr = len(arr) - 2

    ans[len(arr) - 1] = -1
    while curr >= 0:

        if arr[curr] < arr[curr + 1]:
            # ans.append(arr[curr + 1])
            ans[curr] = arr[curr + 1]
            if arr[curr + 1] > stack[-1]:
                stack.append(arr[curr + 1])
        else:
            stackTop = stack[-1]
            ansTop = ans[curr + 1]
            # print(arr[curr], stackTop, ansTop)
            if ansTop > arr[curr]:
                ans[curr] = ansTop

            elif stackTop > arr[curr]:
                # ans.append(stack[-1])
                ans[curr] = stackTop
            else:
                # ans.append(-1)
                ans[curr] = -1
                stack.append(arr[curr])
        curr = curr - 1
    print(stack)
    return ans


arr = [int(i) for i in input().strip().split()]

ans = findNextGreater(arr)
print(ans)
