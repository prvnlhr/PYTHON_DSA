def timeTaken(co, io):
    count = 0
    while len(co) > 0:
        if check(co, io) == True:
            co = co[1:]
            io = io[1:]
            count += 1
        else:
            co = co[1:n] + co[:1]
            count += 1
    return count


def check(co, io):
    if (co[0] == io[0]):
        return True
    return False


n = int(input())
co = [int(i) for i in input().strip().split()]
io = [int(j) for j in input().strip().split()]
ans = timeTaken(co, io)
print(ans)
