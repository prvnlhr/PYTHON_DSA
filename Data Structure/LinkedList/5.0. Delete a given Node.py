class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteNode(head, x):
    prev = head
    main = head
    if head == x:
        head = head.next
        return head

    while main:
        if main.data == x:
            prev.next = main.next

        prev = main
        main = main.next

    return head


def deleteANode(head, x):
    if (head.data == x):
        head = head.next
        return head
    curr = head
    while (curr is not None):
        if (curr.data == x):
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next
    return head


# __Main_____________________________________________________________________________________________________________________
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
x = int(input())
l = deleteNode(l, x)
printll(l)
