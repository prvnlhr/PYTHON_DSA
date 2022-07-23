def printSubsetHelper(arr , lst):
    n = len(arr)
    if (n==0):
        for num in lst:
            print(num , end=' ')
        print()
        return
    printSubsetHelper(arr[1:]  , lst)
    newLst =  lst.copy()
    newLst.append(arr[0])
    printSubsetHelper(arr[1:] , newLst)
    return

def printsubset(arr):
    printSubsetHelper(arr , [])


n = int(input())
arr  = list(int(i) for i in  input().strip().split(' '))
printsubset(arr)



