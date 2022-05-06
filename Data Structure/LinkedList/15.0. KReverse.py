class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def KReverse(head, n):
    if (head == None or n <= 1):
        return head
    elif (head.next == None):
        return head

    prev = head
    curr = prev.next
    i = 1
    prev.next = None

    while curr and i < n:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i = i + 1
    head.next = KReverse(curr, n)
    return prev


# _Main_________________________________________________________________________________________________________________

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
head = KReverse(head, 3)
printLL(head)
