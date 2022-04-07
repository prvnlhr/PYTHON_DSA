# You have been given an array/list ‘arr’ of length ‘N’, which
# contains single digit elements at every index. Your task is
# to return the sum of all elements of the array. But the final
# sum should also be a single digit.

# For the given array [5, 8, 4, 9]
#
# The sum of the elements of the array will be
# 5 + 8 + 4 + 9 = 26.
# Since 26 is not a single-digit number, we will again take the sum of the digits of 26.
# 2 + 6 = 8.
# Now 8 is a single-digit number. So we will stop here and return 8.
#
# We will iterate from left to right and will calculate the sum of
# the elements and if the sum becomes a double-digit number we will
# make it a single-digit number according to the steps given in the
# problem statement.


# 1. Create a variable ‘SUM’ of type integer and initialize it with zero.
# 2. Start iterating the array from left to right and add the current element to the sum.
# 3. If ‘SUM’ is greater than 9, create another variable ‘digitsSum’, and store the sum
#    of digits of the variable ‘SUM’ in it.
# 4. Then update ‘SUM’ as ‘digitsSum’.
# 5. Finally, output the ‘SUM’.
#
def ArraySpecialSum(n, arr):
    sum = 0

    for i in range(len(arr)):

        sum = sum + arr[i]
        if sum >= 10:
            # Find sum of all the digits of currSum
            digit1 = sum % 10
            digit2 = sum // 10
            digitsSum = digit1 + digit2

            sum = digitsSum  # update sum

    return sum


n = int(input())
arr = [int(i) for i in input().split()]
print(ArraySpecialSum(n, arr))
