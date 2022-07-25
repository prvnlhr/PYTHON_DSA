import sys

sys.setrecursionlimit(10 ** 8)


def subsetsSccumK(arr, k):

    return subsetsSumKHeleper(arr, 0 , k)


def subsetsSumKHeleper(arr, si , k):

    if si == len(arr):
        if k == 0:
            return [list()]
        else:
            return list()

    smalloutput1 = subsetsSumKHeleper(arr , si+1 , k)
    smalloutput2 = subsetsSumKHeleper(arr , si+1 , (k - (arr[si]-1)))
    output = (len(smalloutput1) + len(smalloutput2)) * [0]

    index = 0
    for i in range(len(smalloutput1)):
        output[index] = smalloutput1[i]
        index +=1

    for i in range(len(smalloutput2)):
        output[index] = (len(smalloutput2[i]) +1 ) * [0]
        output[index][0] = arr[si]

        # for j in range(len(smalloutput2[i])):
        #     output[index][j+1] = smalloutput2[i][j]
        # index +=1
    return output


def subsetsSumK(arr, k):
    n = len(arr)
    if n == 1:
        if arr[0] == k:
            output = [[k]]
            return output
        else:
            output = []
            return output
    output1 = subsetsSumK(arr[:-1], k)
    output2 = subsetsSumK(arr[:-1], k - arr[-1])
    for lst in output2:
        lst.append(arr[-1])

    if arr[-1] == k:
        output2.append([k])
    return output1 + output2








# taking input
def takeInput():
    n = int(input().strip())

    if n == 0:
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


# printing the list of lists
def printListOfList(liOfLi):
    for li in liOfLi:
        for elem in li:
            print(elem, end=" ")
        print()


# main
arr, n = takeInput()

if n != 0:
    k = int(input().strip())
    liOfLi = subsetsSumK(arr, k)

    printListOfList(liOfLi)
