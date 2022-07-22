def LastIndex(arr, x):

    res  = LastIndexHelper(arr , x , 0 , -1)
    return res

def LastIndexHelper(arr, x, i , li):

    l = len(arr)
    if l == 0:
        return -1
    if i == l:
        if li==-1:
            return -1
        else:
            return li

    if arr[i] == x:
        li = i
    i = i+1
    index = LastIndexHelper(arr , x , i , li)
    return index


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
ans = LastIndex(arr, x)
print(ans)
