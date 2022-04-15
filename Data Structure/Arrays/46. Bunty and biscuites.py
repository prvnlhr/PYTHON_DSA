def biscuites(N, A, B):
    maxMoney = float('inf')
    for x in range(1, N):
        currMoney = A * (x * x) + B * ((N - x) * (N - x))
        maxMoney = min(maxMoney, currMoney)

    return maxMoney


N = int(input())
A = int(input())
B = int(input())
print(N, A, B)
ans = biscuites(N, A, B)
print(ans)
