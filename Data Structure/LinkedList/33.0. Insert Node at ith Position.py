# __Creating Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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


def insertAtith(head, i, element):
    newNode = Node(element)
    temp = head
    currPos = 1

    # Edge case::
    if i == 0:
        newNode.next = head.next
        head = newNode
        return head

    # 1. Looping through the LL
    while temp is not None:

        # 2. if position reached
        if currPos == i:
            newNode.next = temp.next
            temp.next = newNode
            return head

        # 3. moving pointers
        temp = temp.next
        currPos = currPos + 1

    return head


def insertAtithRec(head, i, element):
    # ex: 1 2 3 4 5 6
    # i = 3
    #  element = 7
    if i < 0:
        return head

    if i == 0:
        # at  i = 0 , head = 4
        newNode = Node(element)
        #  newNode = 7
        newNode.next = head
        # 7->4
        return newNode  # return 7

    smallHead = insertAtithRec(head.next, i - 1, element)
    # smallHead = 7 , address of 7 i.e newNode
    head.next = smallHead
    # here head == 3 , i.e previous node because for head ==4 call has completed
    # 3->7
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
i = int(input())
element = int(input())
newLL = insertAtithRec(head, i, element)
printLL(newLL)
