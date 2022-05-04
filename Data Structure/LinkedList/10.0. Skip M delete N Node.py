class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def SkipMDeleteN(head, M, N):
    if M == 0:
        return None
    if N == 0:
        return head

    skip_ptr = head
    while skip_ptr and skip_ptr.next:

        # This loop is for skipping M elements :
        for i in range(1, M):
            skip_ptr = skip_ptr.next
        if skip_ptr.next is None:
            return head
        del_ptr = skip_ptr.next

        # This loop is for deleting N elements by making new connection at end of this loop
        for j in range(0, N):
            del_ptr = del_ptr.next
        # deleting nodes by making connection
        skip_ptr.next = del_ptr
        skip_ptr = skip_ptr.next
    return head


def skipMdeleteN(head, M, N):
    if M == 0:
        return None
    if N == 0:
        return head
    curr = head
    temp = None

    while curr != None:
        take = 0
        skip = 0

        while curr != None and take < M:
            if temp == None:
                temp = curr
            else:
                temp.next = curr
                temp = curr
            curr = curr.next
            take = take + 1

        while curr != None and skip < N:
            newNode = curr
            curr = newNode.next
            skip = skip + 1
    if temp != None:
        temp.next = None
    return head


'''Self solved'''


def skipMN(head, M, N):
    curr = head
    countM = 1

    while curr:
        '''if countM is equal to M then delete N nodes'''
        if countM == M:
            countN = 0
            countM = 1
            prev = curr
            while curr and countN <= N:
                curr = curr.next
                countN += 1

            '''make connections to delete N elements'''
            prev.next = curr
            '''reset countM to 1'''

        else:
            '''else skip M Nodes'''
            countM += 1
            curr = curr.next

    return head


def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


# Main
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
m = int(input())
n = int(input())
l = skipMN(l, m, n)
# l = skipMdeleteN(l, m, n)
# l = SkipMDeleteN(l, m, n)
printll(l)
