class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def startingPointOfLoop(head):
    loopExist = False
    # Edge cases:
    if head is None:
        return
    if head.next is None:
        return

    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loopExist = True
            break

    # if loop exist
    if loopExist:
        slow = head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

        return slow.next.data
    else:
        return loopExist


# ________________________________________________________________________________________________
# _ALL CYCLE RELATED PROGRAMS : DETECT, START, REMOVE _______________________________________________________________________________________________
def detectLoop(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return 'Loop Detected'
    return 'No Loop'


def detectStartOfLoop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow.data


def detectAndDelete(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    slow = head

    prev = fast
    while slow != fast:
        prev = fast
        slow = slow.next
        fast = fast.next
    prev.next = None


# __________________________________________________________________________________________________
def printLoopWalaLL(head):
    times = 20
    count = 0

    while head:
        print(head.data, end=' ')
        head = head.next
        if count == times:
            break
        count += 1
    print()


# __Printing LL function _______________________________________________________________________________________________
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    # print(None)
    return


# Program to detect loop and remove if exist
# head = takeInput()
# creating Loop for testing:__________________________
# 50->20->15->4->10->15
# head.next.next.next.next.next = head.next.next
# 1->2->3->4->5->
# head.next.next.next.next.next = head.next
# ____________________________________________________
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
eight.next = three
head = one

# fifty = Node(50)
# twenty = Node(20)
# fifteen = Node(15)
# four = Node(4)
# ten = Node(10)
# fifty.next = twenty
# twenty.next = fifteen
# fifteen.next = four
# four.next = ten
# ten.next = fifteen
# head = fifty
# printLL(head)


isLoop = detectLoop(head)
print(isLoop)
printLoopWalaLL(head)
startOfLoop = detectStartOfLoop(head)
print('start :', startOfLoop)
ans = detectAndDelete(head)
printLL(head)

# print()

# if ans == False:
#     print('No Loop exist')
# else:
#     print('starting point of Loop:', ans)
