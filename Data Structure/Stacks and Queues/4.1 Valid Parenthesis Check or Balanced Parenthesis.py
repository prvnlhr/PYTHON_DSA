def validParanthesis(s):
    stack = []

    curr = 0
    ans = False

    while curr < len(s):
        ele = s[curr]
        if ele == '{' or ele == '[' or ele == '(':
            stack.append(ele)

        else:
            top = stack[-1]
            if ele == '}' and top == '{':
                ans = True
                stack.pop()

            elif ele == ')' and top == '(':
                ans = True
                stack.pop()

            elif ele == ']' and top == '[':
                ans = True
                stack.pop()
        curr = curr + 1

    if len(stack) == 0:
        return True
    else:
        return False


s = input()
print(validParanthesis(s))
