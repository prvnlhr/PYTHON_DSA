def staircase(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    ans1 = staircase(n - 1)
    ans2 = staircase(n - 2)
    ans3 = staircase(n - 3)
    return ans1 + ans2 + ans3


n = int(input())
res = staircase(n)
print(res)
