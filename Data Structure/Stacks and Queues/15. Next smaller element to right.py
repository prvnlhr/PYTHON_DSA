# NEAREST SMALLEST TO RIGHT OR NEXT SMALLER TO RIGHT
def NSE(arr):
    stack = []
    n = len(arr)
    ans = [-1 for i in range(n)]

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(arr[i])
    return ans


arr = [int(i) for i in input().strip().split()]
ans = NSE(arr)
print(ans)
