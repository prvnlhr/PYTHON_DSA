from sys import stdin


# Following is the ListNode class already written for the Linked List
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverseBetween(head, m, n):
    if m == n:
        return head

    dummyNode = ListNode(0)
    dummyNode.next = head
    prev = dummyNode

    #    prev
    #     |
    #     0 --> 1 --> 2 --> 3 --> 4 --> 5
    #     |
    #   dummyNode

    # STEP 1__. Moving prev ptr to m pos node
    for i in range(m - 1):
        prev = prev.next

    # reverse the [m, n] nodes

    #          prev
    #           |
    #     0 --> 1 --> 2 --> 3 --> 4 --> 5
    #

    reverse = None
    cur = prev.next
    # FIG 1 :
    #          prev
    #           |
    #     0 --> 1 --> 2 --> 3 --> 4 --> 5
    #                 |
    #                curr
    #
    # STEP 2__. reverse connection from m to n

    for i in range(n - m + 1):
        next = cur.next
        cur.next = reverse
        reverse = cur
        cur = next
    #
    # FIG 2 :
    #          prev             reverse
    #           |                 |
    #     0 --> 1 --> 2 --> 3 --> 4 --> 5
    #                                   |
    #                                  curr

    print(cur.val, end=' ')
    print(prev.val, end=' ')
    print(reverse.val, end=' ')
    print(prev.next.val, end=' ')

    # FIG 3 :
    #          prev          reverse
    #           |               |
    #     0 --> 1 --> 2 <- 3 <- 4 --> 5
    #                 |         |     |
    #                reversed part   curr

    #   elements from position m == 2 and n == 4 has been reversed by reversing connection.

    # now , we want   1 --> 4 --> 3 --> 2 --> 5
    # so in fig 3 , we have to make 1(prev) point to 4(rev) and 2(prev.next) point to 5(curr)
    #
    # STEP 3__. finally making connection to print LL properly (IMP STEP)
    prev.next.next = cur
    prev.next = reverse
    #   0 --> 1 --> 4 --> 3 --> 2 --> 5
    return dummyNode.next


def ReverseIt(head, m, n):
    prev = None
    current = head
    pos = n - m
    count = 0
    initial = current
    while (current is not None):
        # print(count,pos)
        if count > pos:
            break
        next = current.next
        current.next = prev
        prev = current
        current = next
        count = count + 1
    head = prev
    # print('curr', current.val, 'prev', prev.val, initial.val)
    # prev.next = current
    initial.next = current
    # printLinkedList(head)
    # printLinkedList(current)
    return head


def reverseBetween1(head, m, n):
    if n - m == 0:
        return head
    if m == 1:
        if n - m == 1:
            temp = head.val
            head.val = head.next.val
            head.next.val = temp
            return head

    ptr = head
    count = 1
    prev = None
    while ptr and count < m:
        prev = ptr
        ptr = ptr.next
        count = count + 1
    ll = ReverseIt(ptr, m, n)
    if prev:
        prev.next = ll
        return head
    else:
        return ll


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


# _________________________________________________________________________________________


def rev(head, m, n):
    numNodes = n - m + 1
    countN = 0
    prev = head
    main = head

    while main and countN < numNodes:
        nextt = main.next
        main.next = prev
        prev = main
        main = nextt
        countN += 1
    head.next = nextt
    return prev


def revMtoN(head, m, n):
    countM = 1
    sentinal = ListNode(0)
    sentinal.next = head
    curr = sentinal.next
    prev = sentinal

    while curr and countM < m:
        prev = curr
        curr = curr.next
        countM += 1

    revPartHead = rev(curr, m, n)
    prev.next = revPartHead
    return sentinal.next


# _________________________________________________________________________________________

# main

head = takeInput()
m = int(input())
n = int(input())
newLL = revMtoN(head, m, n)
print()
printLinkedList(newLL)
