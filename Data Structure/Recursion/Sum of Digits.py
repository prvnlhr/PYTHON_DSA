def digitSum(n):
    if n == 0:
        return 0
    a = n // 10
    sum = digitSum(a)
    return sum + n % 10


n = int(input())
print(digitSum(n))
