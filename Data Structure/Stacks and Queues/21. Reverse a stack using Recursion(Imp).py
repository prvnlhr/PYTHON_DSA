# NOTE:: JUST MUG UP THIS SOLUTION BECAUSE IT IS A TECHNIQUE TO STORE ,
# THE VALUES IN CALL STACK OF FUNCTION TO REVERSE THE STACK
# SIMILAR SOLUTION IS USED FOR SORTING A STACK USING RECURSION


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
