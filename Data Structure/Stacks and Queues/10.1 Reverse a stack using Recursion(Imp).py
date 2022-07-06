def insertAtBottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
    else:
        temp = stack.pop()
        insertAtBottom(stack, item)
        stack.append(temp)


def reverse(stack):
    if len(stack) != 0:
        temp = stack.pop()
        reverse(stack)
        insertAtBottom(stack, temp)


s = [int(i) for i in input().strip().split()]
reverse(s)
print(s)
