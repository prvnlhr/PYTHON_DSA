from sys import stdin


# Following is the ListNode class already written for the Linked List
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def lengthOfLL(ptr):
    count = 0
    while ptr:
        count = count + 1
        ptr = ptr.next
    return count


pos = 0


def recursiveHelper(ptr):
    global pos
    if ptr == None:
        return 0
    smallAns = recursiveHelper(ptr.next)
    smallAns = smallAns + ptr.val * 2 ** pos
    pos = pos + 1
    return smallAns


def getDecimalValueRecursive(ptr):
    # length = lengthOfLL(ptr)
    ans = recursiveHelper(ptr)
    return ans


def getDecimalValue(head):
    ptr = head
    res = 0
    while ptr:
        print(res)
        res = (res << 1) + ptr.val
        # res << 1:
        # << shift operator used for power here
        # res << 1 --> res * 2**1
        # if res << 2 --> res * 2**2

        ptr = ptr.next

    return res


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
ans = getDecimalValueRecursive(head)
print(ans)
