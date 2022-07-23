def permutations(string):
    l = []
    length = len(string)
    if length == 1:
        return [string]
    for i in range(0, length):
        permu = permutations(string[0:i] + string[i + 1:])
        for perm in permu:
            l.append(string[i] + perm)
    return l


string = input()
ans = permutations(string)
for ans in ans:
    print(ans)
