class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


carry = 0


def addOneToLLHelper(head):
    if head is None:
        return 1

    res = head.val + addOneToLLHelper(head.next)

    head.val = int((res) % 10)
    return int((res) / 10)


def addOneToLL(head):
    carry = addOneToLLHelper(head)
    if carry != 0:
        newNode = ListNode(carry)
        newNode.val = carry
        newNode.next = head
        return newNode
    else:
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
newLL = addOneToLL(l)
# solve(l, n)
printll(newLL)
