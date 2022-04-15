def findMedian(arr1, arr2):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    m = len(arr1)
    n = len(arr2)
    lo = 0
    hi = m

    totalElements = m + n + 1
    elementsOnLeftHalf = totalElements // 2

    while lo <= hi:
        partitionX = (lo + hi) // 2
        partitionY = elementsOnLeftHalf - partitionX

        left1 = float('-inf') if partitionX == 0 else arr1[partitionX - 1]
        left2 = float('-inf') if partitionY == 0 else arr2[partitionY - 1]
        right1 = float('inf') if partitionX == m else arr1[partitionX]
        right2 = float('inf') if partitionY == n else arr2[partitionY]

        if left1 <= right2 and left2 <= right2:
            if (m + n) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) // 2.0


            else:
                return max(left1, left2)

        elif left1 > right2:
            hi = partitionX - 1
        else:
            lo = partitionX + 1


arr1 = [7, 12, 14, 15]
arr2 = [1, 2, 3, 4, 9, 11]

# arr1 = [int(i) for i in input().strip().split()]
# arr2 = [int(j) for j in input().strip().split()]
print(findMedian(arr1, arr2))
