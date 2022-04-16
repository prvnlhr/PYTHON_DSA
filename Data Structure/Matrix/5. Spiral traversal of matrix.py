def spiralTraversal(mat):
    rows = len(mat)
    cols = len(mat[0])
    # SEE TECH DOSE YOUTUBE VIDEO
    dir = 0
    top = 0
    down = rows - 1
    left = 0
    right = cols - 1
    res = []
    while top <= down and left <= right:
        # left->right
        if dir == 0:
            for i in range(left, right + 1):
                res.append(mat[top][i])
            top = top + 1

        # top -->down
        elif dir == 1:
            for i in range(top, down + 1):
                res.append(mat[i][right])

            right = right - 1

        # right-->left
        elif dir == 2:
            for i in range(right, left - 1, -1):
                res.append(mat[down][i])
            down = down - 1

        # down-->top
        elif dir == 3:
            for i in range(down, top - 1, -1):
                res.append(mat[i][left])
            left = left + 1

        # This will always keep dir from 0 to 3
        dir = (dir + 1) % 4
    return res


mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
ans = spiralTraversal(mat)
print('req', '1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10')
print(ans)
