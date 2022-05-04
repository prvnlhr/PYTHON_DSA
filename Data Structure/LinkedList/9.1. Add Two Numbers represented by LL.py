class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def addTwoLL(l1, l2):
    temp1 = l1
    temp2 = l2
    carry = 0
    newll = None
    newllTail = None
    while temp1 or temp2:

        # calculating the addition:
        if temp1 and temp2:
            addition = (temp1.val + temp2.val) + carry
        elif temp1:
            addition = temp1.val + carry
        elif temp2:
            addition = temp2.val + carry

        # creating newNode:
        newData = addition % 10
        carry = addition // 10
        newNode = ListNode(newData)

        # adding newNode to newLL
        if newll == None:
            newll = newNode
            newllTail = newNode
        else:
            newllTail.next = newNode
            newllTail = newNode

        # moving temp1 and temp2 to next node
        if temp1:
            temp1 = temp1.next
        if temp2:
            temp2 = temp2.next
    # Ending: Checking if carry > 1 then add extra newNode
    if carry != 0:
        newNode = ListNode(carry)
        newllTail.next = newNode

    return newll


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
head1 = takeInput()
head2 = takeInput()
newll = addTwoLL(head1, head2)
printLL(newll)
