class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# You are given the head of a singly linked-list. The list can be represented as:
# INPUT LIST :
# L0 → L1 → L2 → L4 → L5 ... → Ln - 1 → Ln
#
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# For list [1,2,3,4,5,6,7] we need to return [1,7,2,6,3,5,4].

# We can note, that it is actually two lists [1,2,3,4] and [7,6,5],
# where elements are interchange.


# Geeks for Geeks Solution: O(N) O(N)
def reorderListGfg(head):
    if (head is None):
        return None

    temp = head
    ans = []

    while head:
        ans.append(head)
        head = head.next

    if (len(ans) == 1 or len(ans) == 2):
        return temp

    prev = temp
    curr = prev.next
    len_ = len(ans)

    if (len_ % 2 == 0):
        act_ = len_ // 2 - 1

    else:
        act_ = len_ // 2 + 1

    while act_ > 0:
        n = ans.pop()
        n.next = None
        prev.next = n
        prev.next.next = curr
        prev = curr
        curr = curr.next
        act_ -= 1

    curr.next = None

    return head


# CN Solution Recursive
def rearrangeCN(head):
    if (head == None):
        return head
    second = head.next
    prev = second
    if (prev == None):
        return head
    last = prev.next
    if (last == None):
        return head
    # atleast 3 node are present
    while (last.next):
        prev = last
        last = last.next
    #
    head.next = last
    prev.next = None
    last.next = rearrangeCN(second)
    return head


# LeetCodeSolution O(N)
def reorderList(head):
    if head is None or head.next is None:
        return head

    # Calculate the length of the list
    list_len = 0
    cur = head
    while cur is not None:
        list_len += 1
        cur = cur.next

    # Splice the list into the first floor(n/2) nodes and the last ceiling(n/2) nodes
    aux = Node(head)
    l1 = aux
    l2 = head
    for i in range(list_len // 2):
        l1 = l1.next
        l2 = l2.next
    l1.next = None
    l1 = head

    # Reverse the last ceiling(n/2) nodes
    l2 = rev_list(l2)

    # Interleave the two lists
    res = Node(head)
    cur = res

    while l1 is not None and l2 is not None:
        cur.next = l1
        l1 = l1.next
        cur = cur.next
        cur.next = l2
        l2 = l2.next
        cur = cur.next
        cur.next = None

    if l2 is not None:
        cur.next = l2
    return res.next

    # print(l1, "\n", l2)


def rev_list(Node):
    if head is None or head.next is None:
        return head

    res = Node(None)
    cur = head

    while cur is not None:
        tmp = cur.next
        cur.next = None
        tmp2 = res.next
        res.next = cur
        cur.next = tmp2
        cur = tmp
    return res.next


# __________________________________________________________________________________________________
# __________________________________________________________________________________________________

# LEETCODE EASY UNDERSTAND SOLUTION__
# T: O(N), S: O(N)
def reorderListLC(head):
    #
    if not head:
        return []

    # STEP__1: find middle
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    print(slow.data, fast.data)

    # STEP__2: reverse second half
    prev = None
    curr = slow.next
    while curr:
        nextt = curr.next
        curr.next = prev
        prev = curr
        curr = nextt
    slow.next = None

    # STEP__3: merge lists
    # head1, head2 = head, prev
    head1 = head
    head2 = prev

    ''' IMP STEP COMPLICATED'''
    while head2:
        # saving nextt pointer for moving
        # in below steps , we are basically juggling
        # h1 and h2,from one LL to other in every iteration
        nextt = head1.next
        head1.next = head2
        head1 = head2
        head2 = nextt


# __MAIN__________________________________________________________________________________________
# TakeInput
def takeInput():
    inputList = [int(i) for i in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode
    return head


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    # print(None)
    return


head = takeInput()
reorderListLC(head)
printLL(head)
