class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove(head, n):
    main = head
    count = 0
    while count < n:
        main = main.next
        count += 1
    # Edge case
    # for n == length of LL
    if not main:
        head = head.next
        return head
    ref = head
    prev = head
    while main:
        prev = ref
        ref = ref.next
        main = main.next

    prev.next = ref.next
    return head


def removeNthFromEnd(head, n):
    dummyNode = ListNode(0)
    dummyNode.next = head
    prev = dummyNode
    ref = head
    main = head
    count = 0
    while count < n:
        count = count + 1
        ref = ref.next
    while ref:
        prev = main
        main = main.next
        ref = ref.next
    prev.next = main.next
    return dummyNode.next

    # print(prev.val, main.val)


# _Main________________________________________________________________________
def ll(arr):
    if len(arr) == 0:
        return None
    head = ListNode(arr[0])
    last = head
    for val in arr[1:]:
        last.next = ListNode(val)
        last = last.next
    return head


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
n = int(input())
# head = removeNthFromEnd(l, n)
head = remove(l, n)
(printll(head))
