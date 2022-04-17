def transpose(mat):
    rows = len(mat)
    cols = len(mat[0])

    for i in range(rows):
        for j in range(i, cols):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat


def swapRows(mat):
    rows = len(mat)
    i = 0
    j = rows - 1

    while i < j:
        mat[i], mat[j] = mat[j], mat[i]
        i = i + 1
        j = j - 1
    return mat


def rotate(mat):
    transpose(mat)
    swapRows(mat)
    return mat


testCases = [[[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]], [[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 8, 9]]]

for mat in testCases:
    for a in mat:
        print(a)
    ans = rotate(mat)
    print()
    for x in ans:
        print(x)
    print("__________________________________")
