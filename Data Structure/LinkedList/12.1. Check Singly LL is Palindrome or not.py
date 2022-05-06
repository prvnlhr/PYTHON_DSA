class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(node):
    if node is None or node.next is None:
        return node

    smallHead = reverse(node.next)
    next = node.next
    next.next = node
    node.next = None
    return smallHead


def palindromeLL(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    head2 = reverse(slow)
    slow.next = None
    printLL(head)
    print()
    printLL(head2)
    ptr1 = head
    ptr2 = head2
    while ptr1 and ptr2:

        if ptr1.val != ptr2.val:
            return False
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return True


def takeInput():
    inputList = [int(i) for i in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = ListNode(currData)
        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode
    return head


# __Printing LL function _______________________________________________________________________________________________
def printLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    # print(None)
    return


# Program to detect loop and remove if exist
head = takeInput()
ans = palindromeLL(head)
print(ans)
