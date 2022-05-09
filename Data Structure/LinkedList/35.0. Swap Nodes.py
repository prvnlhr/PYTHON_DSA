class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def swap_nodes(head, i, j):
    curr = head
    prev = previ = curri = prevj = currj = None
    while curr != None:
        if curr.data == i:
            previ = prev
            curri = curr
        elif curr.data == j:
            prevj = prev
            currj = curr

        prev = curr
        curr = curr.next

    if curri == None or currj == None:
        return

    if previ == None:
        head = currj
    else:
        previ.next = currj

    if prevj == None:
        head = curri
    else:
        prevj.next = curri

    curr = curri.next
    curri.next = currj.next
    currj.next = curr

    return head


#
# def swap_nodes(head, i, j):
#     curr = head
#     prev = previ = curri = prevj = currj = None
#     while curr != None:
#         if curr.data == i:
#             previ = prev
#             curri = curr
#         elif curr.data == j:
#             prevj = prev
#             currj = curr
#
#         prev = curr
#         curr = curr.next
#
#     if curri == None or currj == None:
#         return
#
#     if previ == None:
#         head = currj
#     else:
#         previ.next = currj
#
#     if prevj == None:
#         head = curri
#     else:
#         prevj.next = curri
#
#     curr = curri.next
#     curri.next = currj.next
#     currj.next = curr
#
#     return head


def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


# __Printing LL function _______________________________________________________________________________________________
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    # print(None)
    return


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i = int(input())
j = int(input())
index = swap_nodes(l, i, j)
printLL(index)
