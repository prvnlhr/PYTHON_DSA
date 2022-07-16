def productArr(arr):
    n = len(arr)
    leftProd = [1] * n
    rightProd = [1] * n
    for i in range(1, n):
        leftProd[i] = leftProd[i - 1] * arr[i - 1]

    for j in range(n - 2, -1, -1):
        rightProd[j] = rightProd[j + 1] * arr[j + 1]
    res = [1] * n
    for i in range(n):
        res[i] = leftProd[i] * rightProd[i]
    return res


def productArrBetter(arr):
    n = len(arr)
    leftProd = [1] * n

    for i in range(1, n):
        leftProd[i] = leftProd[i - 1] * arr[i - 1]

    res = [1] * n
    temp = 1
    for j in range(n - 1, -1, -1):
        res[j] = temp * leftProd[j]
        temp = arr[j] * temp
    return res


# Input: arr[]  = {10, 3, 5, 6, 2}
# Output: prod[]  = {180, 600, 360, 300, 900}
# 3 * 5 * 6 * 2 product of other array
# elements except 10 is 180
# 10 * 5 * 6 * 2 product of other array
# elements except 3 is 600
# 10 * 3 * 6 * 2 product of other array
# elements except 5 is 360
# 10 * 3 * 5 * 2 product of other array
# elements except 6 is 300
# 10 * 3 * 6 * 5 product of other array
# elements except 2 is 900
#
#
# Input: arr[]  = {1, 2, 3, 4, 5}
# Output: prod[]  = {120, 60, 40, 30, 24 }
# 2 * 3 * 4 * 5  product of other array
# elements except 1 is 120
# 1 * 3 * 4 * 5  product of other array
# elements except 2 is 60
# 1 * 2 * 4 * 5  product of other array
# elements except 3 is 40
# 1 * 2 * 3 * 5  product of other array
# elements except 4 is 30
# 1 * 2 * 3 * 4  product of other array
# elements except 5 is 24


# NAIVE APPROACH::
# WE CAN TRAVERSE THE ARRAY AND FIND PRODUCT OF ALL ELEMENTS
# THEN AGAIN TRAVERSE THE WHOLE ARRAY, and THEN USE // DIVISION
# OPERATOR, AND FIND THE PRODUCT AT A PARTICULAR, ELEMENT EXCEPT
# ITSELF BY DIVIDING THAT ELEMENT.
# THIS WILL TAKE O(N), BUT AS WE ARE NOT ALLOWED TO USE,
# DIVISION OPERATOR, WE WILL HAVE TO FIGURE ANOTHER WAY


# EFFICIENT APPROACH::
# T: O(N)   S: O(N+N)
# THIS IS ALSO O(N) APPROACH BUT HERE WE WLL USE EXTRA ARRAYS
# Approach: Create two extra space, i.e. two extra arrays to store
# the product of all the array elements from start, up to that index
# and another array to store the product of all the array elements
# from the end of the array to that index.
# To get the product excluding that index, multiply the prefix
# product up to index i-1 with the suffix product up to index i+1


# BEST SOLUTION O(N), O(N)


# APPROACH ::
# Maintain the product array for output
# Traverse the array from left to right, and for a index,
# find the product off all elements up to that index,
# excluding that index, EX_   1  2   3  4   5
#                             1  1   2  6  24
# Now, traverse from right to left,
# Maintain a temp variable, which will keep products,
# of elements from right to left.
# now in product array , update the product at that index,
# as product from right elements from temp * product from left i.e product which
# is already store at that index in product
# DRY RUN_________
#
#              1  2  3  4  5
#              1  1  2  6  24    left to right traversal
# temp = 1
#              1  1  2  6  24
# i = 4, last element
# product at product[i] = temp * product[i] == 24  -> 1  1  2  6 24
# temp = 1 * arr[i] = 1 * 5

# i = 3
# product at product[i] = temp * product[i] == 5 * 6 = 30 -> 1  1  2 30  24
# temp = 1 * 5 * arr[i] = 1 * 5 * 4

# SIMILARLY , AFTER ALL TRAVERSAL, 120  60  40  60  24
# SO basically , temp variable is storing product from right to left,
#


def findProduct(arr):
    if len(arr) == 0:
        return 0
    product = [1] * len(arr)

    temp = 1
    for i in range(len(arr)):
        product[i] = temp
        temp = temp * arr[i]

    temp = 1
    for i in range(len(arr) - 1, -1, -1):
        product[i] = product[i] * temp
        temp = temp * arr[i]

    return product


def productUnique(arr):
    productArr = [1] * len(arr)
    productArr[0] = arr[0]
    temp = 1
    for i in range(len(arr)):
        productArr[i] = temp * arr[i]

    rightPro = 1

    for j in range(len(arr) - 1, -1, -1):
        productArr[j] = rightPro * productArr[j]
        rightPro = rightPro * arr[j]
    return productArr


testCases = [[1, 2, 3, 4, 5], [10, 3, 5, 6, 2]]
for arr in testCases:
    ans1 = findProduct(arr)
    # ans2 = productArrBetter(arr)
    # ans3 = productUnique(arr)
    print(ans1)
