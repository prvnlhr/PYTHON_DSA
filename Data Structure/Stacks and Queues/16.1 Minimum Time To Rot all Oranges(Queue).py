import queue

dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def isValid(i, j, rows, cols):
    return 0 <= i < rows and 0 <= j < cols


def minTimeToRotAllOranges(rows, cols, grid):
    q = queue.Queue()
    freshCount = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                q.put([row, col, 0])
            if grid[row][col] == 1:
                freshCount = freshCount + 1
    time = 0
    while not q.empty():
        top = q.get()
        x = top[0]
        y = top[1]
        time = top[2]
        for i in range(len(dir)):
            new_x = x + dir[i][0]
            new_y = y + dir[i][1]
            if isValid(new_x, new_y, rows, cols) and grid[new_x][new_y] == 1:
                freshCount = freshCount - 1
                grid[new_x][new_y] = 2
                q.put([new_x, new_y, time + 1])
    print(freshCount)
    if freshCount > 0:
        return -1
    return time
    # for i in range(rows):
    #     for j in range(cols):
    #         if grid[i][j] == 1:
    #             return -1
    #
    # return time

    # Main_____________


rows = int(input())
cols = int(input())
grid = [[int(i) for i in input().strip().split()] for x in range(rows)]
ans = minTimeToRotAllOranges(rows, cols, grid)
print(ans)
