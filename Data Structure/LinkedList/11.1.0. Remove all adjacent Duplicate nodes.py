class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def adjDuplicates(head):
    if head is None:
        return

    sentinal = ListNode(0)

    sentinal.next = head
    curr = sentinal.next
    prev = sentinal

    while curr:

        if curr.next and curr.val == curr.next.val:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            prev.next = curr.next

        prev = curr
        curr = curr.next
    return sentinal.next


# efficient O(N)
def deleteDuplicate(head):
    if head is None:
        return
        # create a dummy Node:-> sentinel
    sentinel = ListNode(0)
    # sentinel->head
    sentinel.next = head

    # creating a prev node for storing the previous nodes val

    # STEPS:

    prev = sentinel
    curr = head
    # STEPS:
    # if curr == curr.next
    #         (skip all node by moving curr) --> move curr until curr != curr.next
    # remove skipped nodes --> prev.next = curr.next
    # else : if curr != curr.next
    #        --> move prev pointer

    while curr:

        if curr.next and curr.val == curr.next.val:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next
    return sentinel


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
newll = adjDuplicates(l)
# solve(l, n)
printll(newll)
