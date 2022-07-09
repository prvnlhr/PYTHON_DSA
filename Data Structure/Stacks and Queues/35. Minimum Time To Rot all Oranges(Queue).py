import queue

'''

        2   1   1           time = 0
        1   1   0
        0   1   1
        
        2   2   1           time = 1
        2   1   0
        0   1   1
        
        2   2   2           time = 2
        2   2   0
        0   1   1

        2   2   2           time = 3
        2   2   0
        0   2   1           
        
        2   2   2           time = 4
        2   2   0
        0   2   2   
        
   Total time taken = 4 units     
        

'''

#      right    left     down      up
#        |        |        |        |
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
        x, y, time = q.get()

        for i, j in dir:
            new_x = x + i
            new_y = y + j

            if isValid(new_x, new_y, rows, cols) and grid[new_x][new_y] == 1:
                freshCount = freshCount - 1
                grid[new_x][new_y] = 2
                q.put([new_x, new_y, time + 1])

    if freshCount > 0:
        return -1
    return time


rows = 3
cols = 3
# grid = [[int(i) for i in input().strip().split()] for x in range(rows)]
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
ans = minTimeToRotAllOranges(rows, cols, grid)
print(ans)
