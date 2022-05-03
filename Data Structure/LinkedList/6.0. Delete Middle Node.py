# __Creating Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteMiddle(head):
    if (head.next == None):
        return

    if (head.next.next == None):
        return head.next

    slow = head
    fast = head
    prev = None
    while (fast.next != None and fast.next.next != None):
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next
    return head


def deleteMid(head):
    # Base cases
    if (head is None or
            head.next is None):
        return

    # Initialize slow and fast pointers
    # to reach middle of linked list
    slow = head
    fast = head

    # Find the middle and previous of middle
    prev = None

    # To store previous of slow pointer
    while (fast.next is not None and fast.next.next is not None):
        fast = fast.next.next
        prev = slow
        slow = slow.next

    # Delete the middle node
    prev.next = slow.next
    return head


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
        print(head.data, end="->")
        head = head.next
    print(None)
    return


# __Main Driver Function_________________________________________________________________________________________________________________
head = takeInput()
newLL = deleteMiddle(head)
printLL(newLL)
