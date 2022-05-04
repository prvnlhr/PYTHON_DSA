class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def intersection(l1, l2):
    newll = None
    tail = None
    ptr1 = l1
    ptr2 = l2

    while ptr1 and ptr2:

        if ptr1.val == ptr2.val:
            newNode = ListNode(ptr1.val)
            if newll == None:
                newll = newNode
                tail = newll
            else:
                tail.next = newNode
                tail = newNode

            ptr1 = ptr1.next
            ptr2 = ptr2.next

        elif ptr1.val > ptr2.val:
            ptr2 = ptr2.next

        elif ptr2.val > ptr1.val:
            ptr1 = ptr1.next
    return newll


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
head1 = takeInput()
head2 = takeInput()
newll = intersection(head1, head2)
printLL(newll)
