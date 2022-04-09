# CN PROBLEM::
# Ex_1.
# 1 2 3 4 5 6 7 8 9
# [2, 1, 4, 3, 6, 5, 8, 7, 9]

# Ex_2.
# 1 2 3 4 5 6
# [2, 1, 4, 3, 6, 5]


def swapAB(li, n):
    i = 0
    j = 1
    while i < n and j < n:
        li[i], li[j] = li[j], li[i]

        i = i + 2
        j = i + 1


def SwapAlternate(li, n):
    for i in range(0, n - 1, 2):
        # print(li[i])
        li[i], li[i + 1] = li[i + 1], li[i]


# GFG PROBLEM::
# Input: arr[] = {1, 2, 3, 4, 5, 6}
# Output: 6 2 4 3 5 1
# Operation 1: Swap 1 and 6
# Operation 2: Swap 3 and 4
# Input: arr[] = {5, 54, 12, 63, 45}
# Output: 45 54 12 63 5
def swapAlt(li, n):
    i = 0
    j = n - 1

    while i < j:
        li[i], li[j] = li[j], li[i]

        i += 2
        j -= 2
    print(li)


li = [int(i) for i in input().split()]
n = len(li)
swapAB(li, n)
# SwapAlternate(li, n)
# swapAlt(li, n)
print(li)
