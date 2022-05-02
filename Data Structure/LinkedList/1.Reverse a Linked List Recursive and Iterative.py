# __Creating Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseLLIterative(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head


def ReverseRec(head):
    if head is None or head.next is None:
        return head
    smallhead = ReverseRec(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallhead


# _Main_____________________________
# optimise O(n) : By maintaining tail to avoid  traversing again and again from head to last node_______________________
def takeInput():
    inputList = [int(i) for i in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
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
        print(head.data, end=" ")
        head = head.next
    # print(None)
    return


head = takeInput()
head = ReverseRec(head)
printLL(head)
