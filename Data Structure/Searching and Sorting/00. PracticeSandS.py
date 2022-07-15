def productUnique(arr):
    productArr = [1] * len(arr)

    temp = 1
    for i in range(len(arr)):
        productArr[i] = temp
        temp = temp * arr[i]
    print(productArr)

    rightPro = 1

    for j in range(len(arr) - 1, -1, -1):
        productArr[j] = rightPro * productArr[j]
        rightPro = rightPro * arr[j]

    return productArr


testCases = [[1, 2, 3, 4, 5], [10, 3, 5, 6, 2]]
for arr in testCases:
    ans3 = productUnique(arr)
    print(ans3)
