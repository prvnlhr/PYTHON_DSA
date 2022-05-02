class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseKGroup(head, k):
    current = head
    next = None
    prev = None
    count = 0
    # reverse k elements
    while current and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count = count + 1

    # if next element after reversing k is not None
    # call recursive to for next k elements with head = next
    if next:
        head.next = reverseKGroup(next, k)
    return prev


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
head = reverseKGroup(head, 3)
printLL(head)
