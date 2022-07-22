def mul(m , n):
    if n==0 or m==0:
        return 0
    if n>0:
        ans = mul(m , n-1)
        return ans + m
    else:
        ans = mul(m , n+1)
        return ans -m

m = int(input())
n = int(input())
print(mul(m,n))
