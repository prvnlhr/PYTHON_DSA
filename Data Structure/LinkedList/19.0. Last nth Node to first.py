class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def takeInput():
    inputList = [int(i) for i in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = ListNode(currData)
        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode
    return head


# __Printing LL function _______________________________________________________________________________________________
def printLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    # print(None)
    return


# ___________________________________________________________
# Given a LL , bring th nth node from last to first.

# Ex_1.
# 1 2 3 4 5 6 7 8 9 -1
# n = 5
# 5 1 2 3 4 6 7 8 9

# Ex_2.
# 1 2 3 4 5 6 7 8 9 -1
# n = 3
# 7 1 2 3 4 5 6 8 9


# Ex_3.
# 5 4 8 7 6 3 14 5 3 21 4 5 69 -1
# n = 6
# 5 5 4 8 7 6 3 14 3 21 4 5 69


# ___O(N)__________________________________________________
def lastNthNodeToFirst(head, n):
    sentinal = ListNode(0)
    sentinal.next = head
    main = sentinal.next

    countN = 0
    while main and countN < n:
        main = main.next
        countN += 1

    nthNode = sentinal.next
    prev = sentinal
    while main:
        prev = nthNode
        nthNode = nthNode.next
        main = main.next

    prev.next = nthNode.next
    prevHead = sentinal.next
    sentinal.next = nthNode
    nthNode.next = prevHead
    head = nthNode
    return head


head = takeInput()
n = int(input())
newll = lastNthNodeToFirst(head, n)
printLL(newll)
