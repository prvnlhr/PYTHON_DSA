# Problem ID 331 even after odd in a LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# NOTE: We are not arranging on basis of list values, we are
# arranging on basis of even and odd "positions"
# 1 2 3 4 5 6 7 8 9 10 11 12 -1
# 1 3 5 7 9 11 2 4 6 8 10 12


# SELF SOLVED 100%

def evenafterodd(head):
    evenLL = Node(0)

    # evenTail for ending of evenLL
    evenTail = evenLL

    oddLL = Node(0)
    # oddTail for ending of oddLL
    oddTail = oddLL

    # Flag to decide where to add ptr node,
    # at evenLL or oddLL
    flag = 'even'

    # ptr for pointing curr node
    ptr = head
    while ptr is not None:

        if flag == 'even':

            # extract node from LL , to add to respective, even or odd LL
            evenNode = ptr

            # saving next ptr # IMP, or it will break LL
            ptr = ptr.next

            # Attaching extracted node to respective LL
            evenNode.next = None
            evenTail.next = evenNode
            evenTail = evenNode
            flag = 'odd'

        elif flag == 'odd':

            oddNode = ptr
            ptr = ptr.next
            oddNode.next = None
            oddTail.next = oddNode
            oddTail = oddNode
            flag = 'even'

    evenNode.next = oddLL.next
    head = evenLL.next

    printll(head)


def arrange_LinkedList(head):
    # Steps: 1. We will maintain odd and even list
    # 2. We will connect even places to even list and odd places to odd list
    # 3. finally we will connect even list after odd list
    #
    # Corner case
    if (head == None):
        return None

    # Initialize first nodes of
    # even and odd lists
    odd = head
    even = head.next

    # Remember the first node of even list so
    # that we can connect the even list at the
    # end of odd list.
    evenFirst = even

    # infinite loop
    while (1 == 1):

        # If there are no more nodes,
        # then connect first node of even
        # list to the last node of odd list
        if (odd == None or even == None or (even.next) == None):
            odd.next = evenFirst
            break

        # Connecting odd nodes
        odd.next = even.next
        # updating odd
        odd = even.next

        # If there are NO more even nodes
        # after current odd.
        if (odd.next == None):
            even.next = None
            odd.next = evenFirst
            break

        # Connecting even nodes
        even.next = odd.next
        # updating even
        even = odd.next
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
l = arrange_LinkedList(l)
printll(l)
