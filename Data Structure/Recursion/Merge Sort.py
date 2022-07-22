def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return
    mid = len(arr) // 2
    a1 = arr[0:mid]
    a2 = arr[mid:]
    merge_sort(a1)
    merge_sort(a2)
    merge(a1, a2, arr)


def merge(a1, a2, arr):
    i = 0
    j = 0
    k = 0
    print("a1  :", a1)
    print("a2  :", a2)
    print("arr :", arr)
    print()
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            i = i + 1
            k = k + 1
        else:
            arr[k] = a2[j]
            j = j + 1
            k = k + 1

    while i < len(a1):
        arr[k] = a1[i]
        k = k + 1
        i = i + 1
    while j < len(a2):
        arr[k] = a2[j]
        k = k + 1
        j = j + 1


# n = int(input())
# arr = list(int(i) for i in input().strip().split())
arr = [8, 4, 2, 1, 0]
merge_sort(arr)
print(arr)
