# At O(n)_______
# def power(x, n):
#     if n == 0:
#         return 1
#     res = x * power(x, n - 1)
#     return res

# At O(logn)_____
def power(x, n):

    if (n == 0):
        return 1
    temp = power(x, int(n / 2))

    if (n % 2 == 0):
        return temp * temp
    else:
        if (n > 0):
            return x * temp * temp
        else:
            return (temp * temp) / x


str = input().split()
x, n = int(str[0]), int(str[1])
print(power(x, n))


