from collections import defaultdict


# BEST SOLUTION USING HASHMAP.
# The time complexity of this solution is O(m * n)
# and we are doing only one traversal of the matrix.


# INITIALIZE, MAP WITH FIRST ROW ELEMENTS EQUAL TO VALUE 1 ( key : 1)
# THE VALUE FOR KEY REPRESENTS ROW INDEX.
# SO IF LET SAY KEY IS 5:2, means row is 2,
# this states that 5 was found in previous 2 rows.
# So at the end if a key has value equal to no of rows,
# that means it was common in all rows.


def findCommonElement(mat):
    map = defaultdict(list)
    rows = len(mat)
    cols = len(mat[0])
    res = []
    for i, ele in enumerate(mat[0]):
        if ele not in map:
            map[ele] = 1

    # we will start from 1st row not 0th row
    for i in range(1, rows):
        for j in range(cols):
            ele = mat[i][j]
            # Check if key present in map and increase count
            if ele in map and map[ele] == i:
                map[ele] = map[ele] + 1

                # if value for key is equal to rows count, means common element found
                if map[ele] == rows - 1:
                    res.append(ele)
    return res


mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9],
       ]
ans = findCommonElement(mat)
print(ans)
