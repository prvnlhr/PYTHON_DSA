def reverseAStringUsingStack(s):
    stack = []
    curr = 0

    while curr < len(s):
        stack.append(s[curr])
        curr = curr + 1
    ans = ''
    while stack:
        ele = stack[-1]
        ans = ans + ele
        stack.pop()
    return ans


s = input()
print(reverseAStringUsingStack(s))
