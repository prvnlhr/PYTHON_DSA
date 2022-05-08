class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def mergeTwoLists(l1, l2):
    if l1 is None and l2 is None:
        return None

    if l1 is None and l2 is not None:
        return l2
    if l2 is None and l1 is not None:
        return l1

    ptr1 = l1
    ptr2 = l2
    head = None
    currentListNode = None

    if ptr1.val <= ptr2.val:
        head = ptr1
        ptr1 = ptr1.next
    else:
        head = ptr2
        ptr2 = ptr2.next

    currentListNode = head

    while ptr1 is not None and ptr2 is not None:
        if ptr1.val <= ptr2.val:
            currentListNode.next = ptr1
            currentListNode = ptr1
            ptr1 = ptr1.next

        else:
            currentListNode.next = ptr2
            currentListNode = ptr2
            ptr2 = ptr2.next

    # print(newll.val, ptr1.val, ptr2.val)

    if ptr1 is not None:
        currentListNode.next = ptr1
    else:
        currentListNode.next = ptr2

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


def printll(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


# Main
# Read the link list elements including -1
arr1 = list(int(i) for i in input().strip().split(' '))
arr2 = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l1 = ll(arr1[:-1])
l2 = ll(arr2[:-1])
l = mergeTwoLists(l1, l2)
printll(l)
