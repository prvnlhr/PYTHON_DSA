# All elements are in the range from 0 to n-1

# APPROACH 1:
# :The elements in the array is from 0 to n-1 and all of them are positive.
# So to find out the duplicate elements, a HashMap is required, but the question
# is to solve the problem in constant space. There is a catch, the array is of
# length n and the elements are from 0 to n-1 (n elements). The array can be
# used as a HashMap.

# This approach only works for arrays having at most 2 duplicate
# elements i.e It WILL NOT WORK if the array contains MORE THAN 2
# duplicates of an element. For example: {1, 6, 3, 1, 3, 6, 6}
# it will give output as : 1 3 6 6.

# OPTIMISED T: O(N), S: O(1)

def findDuplicates(arr, n):  # It WILL NOT WORK if the array contains MORE THAN 2 DUPLICATES
    res = []
    for num in arr:
        num = abs(num)
        print(num, num - 1)
        if arr[num - 1] < 0:
            print('res', num)
            # if n-1 is -ve we have previously encountered it , so append it to result
            res.append(num)
        else:

            # at num-1 change value to -ve
            arr[num - 1] = -arr[num - 1]
            print(arr)
    return res


# APPROACH 2:____________________________________________________
#  While Traversing the array, if an element ‘a’ is encountered
#  then increase the value of a % n‘th element by n. The frequency
#  can be retrieved by dividing the a % n’th element by n.

# Time Complexity: O(n).
# Only two traversals are needed. So the time complexity is O(n).
# Auxiliary Space: O(1).

def findDups(arr, n):
    # Increase  arr[x]  --> x = ele % n  to -> arr[x] + n
    for i, ele in enumerate(arr):
        x = ele % n
        arr[x] = arr[x] + n

    res = []
    for i in range(len(arr)):
        if arr[i] >= n * 2:
            res.append(i)
    return res


def takeInput():
    n = int(input())
    if n == 0:
        return list(), 0
    arr = [int(i) for i in input().split()]
    return arr, n


t = int(input())

while (t > 0):
    arr, n = takeInput()
    print(findDups(arr, n))
    t = t - 1
