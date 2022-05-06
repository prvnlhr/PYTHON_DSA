class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# O(n)
def findNthNodeFromLast(head, n):
    ref = head
    main = head
    count = 0
    while count < n:
        count = count + 1
        ref = ref.next
    while ref:
        ref = ref.next
        main = main.next
    print(main.val)
    return main


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


# Program to detect loop and remove if exist
head = takeInput()
n = 2
nth = findNthNodeFromLast(head, n)
print(nth.val)
