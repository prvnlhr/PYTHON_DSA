def reverseAStringUsingStack(s):
    stack = []
    curr = 0

    # One by one put a characters of string to stack
    while curr < len(s):
        stack.append(s[curr])
        curr = curr + 1

    # one by one pop elements form stack and make a string
    ans = ''
    while stack:
        ele = stack[-1]
        ans = ans + ele
        stack.pop()
    return ans


s = input()
print(reverseAStringUsingStack(s))
