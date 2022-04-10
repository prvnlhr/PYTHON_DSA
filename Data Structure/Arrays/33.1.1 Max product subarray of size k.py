def productSubArray(arr, k):
    maxProduct = -float('inf')
    windowProduct = 1

    i = 0
    j = 0
    while j < len(arr):

        windowProduct *= arr[j]
        if j - i + 1 >= k:
            maxProduct = max(maxProduct, windowProduct)
            windowProduct = windowProduct // arr[i]
            i = i + 1

        j = j + 1

    return maxProduct


arr = [1, 5, 9, 8, 2, 4, 1, 8, 1, 2]
# arr = [3, -4, 3, -3]
k = 6
ans = productSubArray(arr, k)
print(ans)
