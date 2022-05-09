import heapq


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    # THIS IS CRUCIAL STEP USED TO COMPARE NODES DATA IN MIN HEAP
    # Override the `__lt__()` function to make `Node` class work with min-heap
    def __lt__(self, other):
        return self.val < other.val


def mergeKSortedLL(headsArray):
    min_heap = []

    for head in headsArray:
        min_heap.append(head)

    heapq.heapify(min_heap)

    newHead = None
    tail = None

    while min_heap:
        node = heapq.heappop(min_heap)

        if newHead is None:
            newHead = node
            tail = newHead
        else:
            tail.next = node
            tail = node
        if node.next:
            heapq.heappush(min_heap, node.next)
    return newHead


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


# Input: k = 3, n =  4
# list1 = 1->3->5->7->NULL
# list2 = 2->4->6->8->NULL
# list3 = 0->9->10->11->NULL

k = int(input())
headsArray = []
for i in range(k):
    head = takeInput()
    headsArray.append(head)

newHead = mergeKSortedLL(headsArray)
printLL(newHead)
# for head in headsArray:
#     printLL(head)
#     print()
