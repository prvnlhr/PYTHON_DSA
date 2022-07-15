def search1(arr, x):
    def searchHelper(lo, hi):

        if lo > hi:
            return -1

        mid = (lo + hi) // 2

        if arr[mid] == x:
            return mid

        elif arr[lo] <= arr[mid]:  # left sorted

            if arr[lo] <= x and x <= arr[mid]:
                return searchHelper(lo, mid - 1)
            else:
                return searchHelper(mid + 1, hi)

        elif arr[mid] < arr[hi]:  # right is sorted
            if arr[mid] <= x and x <= arr[hi]:
                return searchHelper(mid + 1, hi)
            else:
                return searchHelper(lo, mid - 1)

    return searchHelper(0, len(arr) - 1)


def searchInRotated(arr, x):
    def search(lo, hi):

        if lo > hi:
            return -1
        mid = (lo + hi) // 2

        if arr[mid] == x:
            return mid

        # AS ARRAY IS ROTATED, WE WILL NEED TO CHECK
        # WHICH PART IS SORTED LEFT OF MID or RIGHT OF MID

        # if left side is sorted____
        elif arr[lo] <= arr[mid]:  # check if key present in this part,
            if arr[lo] <= x and x <= arr[mid]:  # check if key present in this part,then recur
                return search(lo, mid - 1)

            else:  # if not present then, recur on other half part
                return search(mid + 1, hi)

        # SIMILARLY
        elif arr[mid] < arr[hi]:  # if right side is sorted,
            if arr[mid] <= x and x <= arr[hi]:  # check if key present in this part,then recur
                return search(mid + 1, hi)
            else:  # if not present then,recur on other half part
                return search(lo, mid - 1)

    return search(0, len(arr) - 1)


testCases = [[[3, 4, 5, 1, 2], [1]], [[4, 5, 6, 7, 8, 9, 1, 2, 3], [6]], [[5, 6, 7, 8, 9, 10, 1, 2, 3], [3]]]
for test in testCases:
    arr = test[0]
    key = test[1][0]
    ans1 = searchInRotated(arr, key)
    ans2 = search1(arr, key)
    print(ans1, ans2)
