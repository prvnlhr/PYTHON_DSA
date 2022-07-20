count = 0
def countZeros(n):
    global count
    if n==0:
        return 1
    lasdigit = n%10
    if lasdigit == 0:
        count = count+1
    countZeros(n//10)
    return count

n = int(input())
print(countZeros(n))
