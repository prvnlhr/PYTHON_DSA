# Input:  arr[] = {1, 2, 3, 4, 5}
# Output: arr[] = {5, 1, 2, 3, 4}

# SOL 1__. O(N) , EASY
def cyclicRotateArray(arr):
    # Storing last element
    x = arr[len(arr) - 1]

    # shifting array elements by one
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    # assigning first element equal to x
    arr[0] = x
    return arr


# SOL 2__. O(N) , EASY
# i will iterate from 0 to n-1
# j will always be fixed at end ,n-1
def cyclicRotateArray(arr):
    i = 0
    j = len(arr) - 1
    while i < len(arr):
        # swap
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
    print(arr)


arr = [int(i) for i in input().strip().split()]
ans = cyclicRotateArray(arr)
print(ans)
