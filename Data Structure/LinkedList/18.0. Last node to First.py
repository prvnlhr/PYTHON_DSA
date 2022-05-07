class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def moveLastToFirst(head):
    curr = head
    prev = head
    start = head
    while curr.next:
        prev = curr
        curr = curr.next

    curr.next = head
    head = curr
    prev.next = None
    return head


def ll(arr):
    if len(arr) == 0:
        return None
    head = ListNode(arr[0])
    last = head
    for val in arr[1:]:
        last.next = ListNode(val)
        last = last.next
    return head


# _Main________________________________________________________________________


def printll(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


# Main
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
newll = moveLastToFirst(l)
# solve(l, n)
printll(newll)
