class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def findnthNode(head, n):
    temp = head
    while temp:
        if n == 0:
            return temp.val
        n = n - 1
        temp = temp.next
    return -1


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
n = int(input())
nthNode = findnthNode(head, n)
print(nthNode)
