# __Creating Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def rev(head):
    sentinal = Node(0)
    sentinal.next = head
    main = sentinal.next
    prev = sentinal

    while main:
        nextt = main.next
        main.next = prev
        prev = main
        main = nextt
    head.next = None
    return prev


def reverITer(head):
    temp = head
    while temp:
        next = temp.next
        temp.next.next = temp
        temp = next
    return temp


def reverseLLIterative(head):
    curr = head
    prev = None
    while curr:
        # storing the curr.next , so that we can move curr after changing connections
        next = curr.next
        # changing connection
        curr.next = prev

        # moving prev node further
        prev = curr
        # moving curr to stored next
        curr = next

    # at end we will make head as prev
    head = prev
    return head


def ReverseRec(head):
    if head is None or head.next is None:
        return head
    smallhead = ReverseRec(head.next)
    # Here tail is last-node head is second-last node
    #   head --> tail

    tail = head.next
    tail.next = head
    #  tail.next --> head ,,,,
    head.next = None
    #  None <- head <- tail
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
# head = reverseLLIterative(head)
head = rev(head)
printLL(head)
