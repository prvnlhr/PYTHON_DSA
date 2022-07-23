def quickSort(arr, start, end):
    # Please add your code here
    if start >= end:
        return

    pivot_index = partition(arr, start, end)
    quickSort(arr, start, pivot_index - 1)
    quickSort(arr, pivot_index + 1, end)


def partition(a, si, ei):
    pivot = a[si]
    # find number of elements smaller than pivot
    count = 0

    for i in range(si, ei + 1):
        if a[i] < pivot:
            count = count + 1

    a[si + count], a[si] = a[si], a[si + count]
    pivot_index = si + count

    i = si
    j = ei

    while i < j:
        if a[i] < pivot:
            i = i + 1
        elif a[j] >= pivot:
            j = j - 1
        else:
            a[i], a[j] = a[j], a[i]
            i = i + 1
            j = j - 1

    return pivot_index


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n - 1)
for x in arr:
    print(x, end=" ")
