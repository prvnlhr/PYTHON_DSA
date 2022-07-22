import time
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input())
start = time.time()
ans = fib(n)
end = time.time()
print(ans , end - start)
