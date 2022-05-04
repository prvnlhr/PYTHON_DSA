class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def findMiddle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


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
middle = findMiddle(head)
print(middle.val)
