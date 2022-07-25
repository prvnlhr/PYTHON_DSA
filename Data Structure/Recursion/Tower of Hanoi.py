def towerOfHanoi(n, source, aux, dest):
    if n == 1:
        print(source, " ", dest)
        return

    towerOfHanoi(n - 1, source, dest, aux)
    print(source, " ", dest)
    towerOfHanoi(n - 1, aux, source, dest)


n = int(input())
towerOfHanoi(n, 'a', 'b', 'c')
