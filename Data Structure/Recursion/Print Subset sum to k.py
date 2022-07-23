def printSubsetHelper(arr , k , lst):
    n = len(arr)
    if (n==0):
        return
    if n==1:
        if arr[0]==k:
            print(k , *lst)
            return

    printSubsetHelper(arr[:-1] , k   , lst)
    printSubsetHelper(arr[:-1] ,k - arr[-1] , [arr[-1]] + lst)
    if arr[-1] == k:
        print(k ,*lst)

def printsubset(arr , k):
    printSubsetHelper(arr , k , [])



n = int(input())
arr  = list(int(i) for i in  input().strip().split(' '))
k = int(input())

printsubset(arr , k)



