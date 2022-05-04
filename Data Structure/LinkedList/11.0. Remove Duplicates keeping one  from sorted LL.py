class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def prac(head):
    curr = head

    while curr:
        while curr.next and curr.val == curr.next.val:
            curr.next = curr.next.next
        curr = curr.next
    return head


def findNext(temp, mapp):
    while temp:
        ele = temp.val
        if mapp[ele] == 1:
            # print('temp', temp.val)
            return temp
        temp = temp.next


# Self Solved 100% , Time complexity O(N) and Space complexity O(N)
def deleteDuplicates(head):
    ptr = head
    prev = head
    mapp = {}
    while ptr is not None:
        if ptr.val in mapp:
            ele = ptr.val
            mapp[ele] = mapp[ele] + 1
        else:
            ele = ptr.val
            mapp[ele] = 1
        ptr = ptr.next

    curr = head
    first = curr.val
    # Edge case if first node is duplicate
    if mapp[first] > 1:
        ans = findNext(curr.next, mapp)
        curr = ans
        head = curr

    while curr and curr.next:
        currnext = curr.next
        ele = currnext.val
        # print(ele)
        if mapp[ele] > 1:
            ans = findNext(curr.next, mapp)
            # print('ans', ans.val)
            curr.next = ans
        curr = curr.next

    # print(mapp)
    return head


def deleteKeepingOne(head):
    sentinal = ListNode(0)
    sentinal.next = head
    curr = sentinal.next
    prev = sentinal

    while curr:

        if curr.next and curr.val == curr.next.val:

            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            prev.next = curr

        else:
            prev = curr
            curr = curr.next
    return sentinal.next


# efficient O(N)
def deleteDuplicate(head):
    if head is None:
        return
    curr = head
    while curr:
        # get next different node
        while curr.next and curr.val == curr.next.val:
            curr.next = curr.next.next

        curr = curr.next
    return head


# EX__
# 11 11 11 11 12 13 14 15
# 11 12 13 14 15
# Ex_
# 11 12 13 13 13 14 15
# 11 12 13 14 15

# _Main________________________________________________________________________
def ll(arr):
    if len(arr) == 0:
        return None
    head = ListNode(arr[0])
    last = head
    for val in arr[1:]:
        last.next = ListNode(val)
        last = last.next
    return head


def printll(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


# Main
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
newll = deleteKeepingOne(l)
newllP = prac(l)
# solve(l, n)
# printll(newll)
printll(newllP)
