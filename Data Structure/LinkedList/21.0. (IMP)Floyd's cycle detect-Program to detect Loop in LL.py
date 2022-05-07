class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# NOTE:: Floyd cycle detects the loop
#  by matching slow and fast pointer, which can meet
#  inside loop at any position,not necessarily at 'looping point'
# "It does not gives starting point of loop directly"
def detectLoop(head):
    slow = head
    fast = head

    while fast.next:
        slow = slow.next
        fast = fast.next.next
        print(slow.data, fast.data)
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


# head = takeInput()
# 1 2 3 4 5 6 7 8
#         |_____|
# 5->8

# creating Loop for testing:
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
six.next = eight
eight.next = three
seven.next = two
head = one
ans = detectLoop(head)
print(ans)
