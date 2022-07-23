def minArray(lst):
    if len(lst) == 1:
        return lst[0]

    smallmin = minArray(lst[1:])
    min = min(smallmin, lst[0])
    return min


def PrintMin(lst, minSoFar=10000000):
    if len(lst) == 1:
        print(minSoFar)
        return
    newMin = min(minSoFar, lst[0])
    PrintMin(lst[1:], newMin)


PrintMin([1, 2, 3, 4, -2, 8, -8, 6, 7])
