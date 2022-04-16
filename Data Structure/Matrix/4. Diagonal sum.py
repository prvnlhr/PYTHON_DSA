def diagonalSum(mat):
    m = len(mat)
    n = len(mat[0])
    sum1 = 0
    sum2 = 0
    i = 0
    j = n - 1
    while i < n and j >= 0:
        sum1 = sum1 + mat[i][i]
        if i != j:
            sum2 = sum2 + mat[i][j]
        j = j - 1
        i = i + 1
    return sum1 + sum2


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(diagonalSum(mat))
