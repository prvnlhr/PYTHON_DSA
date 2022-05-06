class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lastAppearance(head):
    map = {}
    temp = head
    while (temp is not None):
        if (temp.data in map.keys()):
            map[temp.data] = map[temp.data] + 1
            temp = temp.next

        else:
            map[temp.data] = 1
            temp = temp.next

    print(map)
    temp = head

    while (temp is not None):
        # print(temp.data)
        if (map[temp.data] > 1):
            map[temp.data] = map[temp.data] - 1
            temp = temp.next
        else:
            temp = temp.next
    print(map)

    return head


# __Main_____________________________________________________________________________________________________________________
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
newll = lastAppearance(l)
printll(newll)
