class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def mergeTwoInDecresing(head1, head2):
    if (head1 == None and head2 == None):
        return None
    res = None

    while (head1 != None and head2 != None):
        if (head1.data <= head2.data):

            pointer = head1
            head1 = head1.next
            pointer.next = res
            res = pointer
        else:

            pointer = head2
            head2 = head2.next
            pointer.next = res
            res = pointer

    while (head1 != None):
        pointer = head1
        head1 = head1.next
        pointer.next = res
        res = pointer

    while (head2 != None):
        pointer = head2
        head2 = head2.next
        pointer.next = res
        res = pointer

    return res


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


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    # print(None)
    return


head1 = takeInput()
head2 = takeInput()
newLL = mergeTwoInDecresing(head1, head2)
printLL(newLL)
