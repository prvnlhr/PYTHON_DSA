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


# SELF SOLVED
# INTUITIVE , SIMPLE
# 100 %
def remove(head, val):
    sentinal = ListNode(0)
    sentinal.next = head
    main = sentinal.next
    prev = sentinal

    while main:

        if main.val == val:
            prev.next = main.next
            main = main.next
        else:
            prev = main
            main = main.next
    return sentinal.next


def removeGivenNode(head, val):
    sentinal = ListNode(0)
    sentinal.next = head
    ptr = sentinal

    while ptr and ptr.next:

        if ptr.next.val == val:
            ptr.next = ptr.next.next
        else:
            ptr = ptr.next

    return sentinal.next


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
