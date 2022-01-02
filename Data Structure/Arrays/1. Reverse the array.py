# Time Complexity :
#   O(1/2 * N) => O(N) because , 1/2 is constant

def reverseArray(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        j = j - 1
    return arr


arr = [int(i) for i in input().strip().split()]
ans = reverseArray(arr)
print(ans)
