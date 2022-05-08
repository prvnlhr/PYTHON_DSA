from sys import stdin


# Following is the ListNode class already written for the Linked List
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def palindrome(head, val):
    pass


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
ans = palindrome(head, x)
printLinkedList(ans)
