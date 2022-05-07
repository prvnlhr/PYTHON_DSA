class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detectAndDeleteLoop(head):
    loopExist = False
    # Edge cases:
    if head is None:
        return
    if head.next is None:
        return

    slow = head
    fast = head
    # printLL(head)
    # Floyd cycle to detect Loop
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loopExist = True
            break
    print(slow.data)
    # if loop exist -> remove

    # if loopExist ,
    # slow will start from head
    # fast will start from where it was previously
    # when they will meet we get 'loop point'
    if loopExist:
        slow = head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None
    else:
        return loopExist


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


# Program to detect loop and remove if exist
# head = takeInput()
# creating Loop for testing:
# head.next.next.next.next.next = head.next.next
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
#
one.next = two
two.next = three
three.next = four
four.next = five
five.next = seven
seven.next = eight
eight.next = two

head = one
ans = detectAndDeleteLoop(head)
if ans == False:
    print('No Loop exist')
else:
    print('LinkedList after removing Loop:')
    printLL(head)
