def sortInserted(s, ele):
    if len(s) == 0 or ele > s[-1]:
        s.append(ele)
        return
    else:
        temp = s.pop()
        sortInserted(s, ele)
        s.append(temp)


def sortStack(stack):
    if len(stack) != 0:
        temp = stack.pop()
        sortStack(stack)
        sortInserted(stack, temp)


s = [int(i) for i in input().strip().split()]
sortStack(s)
print(s)
