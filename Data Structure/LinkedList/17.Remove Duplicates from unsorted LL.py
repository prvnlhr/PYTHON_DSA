class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def deleteDuplicates(head):
    mapp = {}
    ptr = head
    sentinal = ListNode(0)
    sentinal.next = head
    prev = sentinal
    curr = head

    while curr:
        ele = curr.val
        if ele in mapp:
            prev.next = curr.next
            curr = curr.next
        else:
            mapp[ele] = 1
            prev = curr
            curr = curr.next

    printll(head)


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
newll = deleteDuplicates(l)
# solve(l, n)
printll(newll)
