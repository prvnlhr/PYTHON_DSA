# Ex =  “2 3 1 * + 9 -“
# O/P -> -4
def evaluateReversePolish(arr):
    stack = []

    i = 0
    while i < len(arr):
        ele = arr[i]
        if ele == '+' or ele == '-' or ele == '*' or ele == '/':
            if stack:
                top1 = stack[-1]
                stack.pop()
                top2 = stack[-1]
                stack.pop()
                # print(top1, top2)
                new = (eval(top2 + ele + top1))
                newFloat = float(new)
                newInt = int(newFloat)
                newStr = str(newInt)
                # print(newFloat)
                stack.append(newStr)
        else:
            stack.append(ele)
        i = i + 1
    # print(stack)
    # floatVal = float(stack[-1])
    # ans = (round(floatVal))
    return stack[-1]


# SIMPLE
def evalRPN(arr):
    operators = ['+', '-', '*', '/']
    stack = []

    for ele in arr:
        if ele in operators:
            currOperator = ele
            val1 = stack.pop()
            val2 = stack.pop()
            if currOperator == '+':
                newVal = val2 + val1
            if currOperator == '-':
                newVal = val2 - val1
            if currOperator == '*':
                newVal = val2 * val1
            if currOperator == '/':
                newVal = int(val2 / val1)
            stack.append(int(newVal))
        else:
            stack.append(int(ele))
    return stack[-1]


arr = [i for i in input().strip().split()]
# x = '/'
# y = eval('6' + x + '132')
# print(round(int(y)))
# print(evaluateReversePolish(arr))

print(evalRPN(arr))
