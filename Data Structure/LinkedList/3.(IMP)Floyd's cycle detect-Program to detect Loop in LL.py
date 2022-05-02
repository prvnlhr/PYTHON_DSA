class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detectLoop(head):
    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


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


# _Main_____________________________
# optimise O(n) : By maintaining tail to avoid  traversing again and again from head to last node_______________________


# __Printing LL function _______________________________________________________________________________________________
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    # print(None)
    return


head = takeInput()
# creating Loop for testing:
head.next.next.next.next = head.next.next
ans = detectLoop(head)
print(ans)
