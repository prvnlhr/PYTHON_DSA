# __Creating Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deletenthNode(head, n):
    prev = None
    temp = head
    if n == 0:
        head = head.next
        return head
    while temp:
        if n == 0:
            prev.next = temp.next
        prev = temp
        temp = temp.next
        n = n - 1
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
n = int(input())
newLL = deletenthNode(head, n)
printLL(newLL)
