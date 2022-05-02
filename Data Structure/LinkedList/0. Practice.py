from sys import stdin


# LL -> 1 2 3 2 4 5 6 7 8 9 2 3 4 2 -1
# n = 2
# after removing n = 2
# 1 3 4 5 6 7 8 9 3 4
# Following is the ListNode class already written for the Linked List
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove(head, x):
    curr = head
    prev = curr
    while curr:
        if curr.val == x:
            prev.next = curr.next
            curr = curr.next
        else:

            prev = curr
            curr = curr.next
    return head


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        val = datas[i]
        newListNode = ListNode(val)

        if head is None:
            head = newListNode
            tail = newListNode

        else:
            tail.next = newListNode
            tail = newListNode

        i += 1

    return head


# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()


# main

head = takeInput()
x = int(input())
# ans = removeGivenNode(head, x)
ans = remove(head, x)
printLinkedList(ans)
