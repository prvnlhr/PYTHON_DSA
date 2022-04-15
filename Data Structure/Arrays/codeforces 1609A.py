def solve():
    n = int(input())
    a = list(map(int, input().split(' ')))

    temp = 1
    for i in range(n):
        while (a[i] % 2 == 0):
            a[i] //= 2
            temp *= 2
    print(a)
    a.sort()
    print(a)

    print(temp)

    a[-1] *= temp

    print(a)

    print(sum(a))


t = int(input())

for i in range(t):
    solve()