class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Split LL into two reverse alternating LL
# OG LL -> 1 2 3 4 5 6 7 -1
# A -> 7 5 3 1
# B -> 6 4 2


def divide(head):
    A = None
    B = None

    curr = head
    flag = 'A'
    while curr:
        if flag == 'A':
            newNode = Node(curr.data)
            newNode.next = A
            A = newNode
            flag = 'B'

        elif flag == 'B':
            newNode = Node(curr.data)
            newNode.next = B
            B = newNode
            flag = 'A'

        curr = curr.next
    printll(A)
    printll(B)


# Self Solved
def DivideIntoTwo(head):
    # A = Node(None)
    # B = Node(None)
    h1 = None
    h2 = None
    flag = 'h1'
    while (head != None):
        # The concept is , we have maintain
        # two heads h1 and h2 as None initially
        # In each iteration,we will pick  head's value
        # and make a new_node and ,then newNode.next = h1
        # newNode -> h1 or newNode -> h2
        # so basically reverse connection
        if flag == 'h1':

            newNode = Node(head.data)
            # reverse connection
            newNode.next = h1
            h1 = newNode
            # changing flag for next iteration for picking alternate
            # head(h1 or h2) in each pass
            flag = 'h2'
            print('h1->', end=' ')
            printll(h1)
        else:
            newNode = Node(head.data)
            newNode.next = h2
            h2 = newNode
            flag = 'h1'
            print('h2->', end=' ')
            printll(h2)
            print()

        head = head.next

    printll(h1)
    printll(h2)


# _Main________________________________________________________________________
def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


# Main
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = divide(l)
