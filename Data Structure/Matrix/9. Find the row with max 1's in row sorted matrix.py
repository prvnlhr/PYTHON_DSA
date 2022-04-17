# MY SOL, EASY UNDERSTANDABLE
# The time complexity is O(m+n)


def maxOneRow(mat):
    rows = len(mat)
    cols = len(mat[0])

    resRowIndex = 0  # store the output row with max one's
    max_ones_col_index = cols - 1  # store the index of col reached from right to left with max 1's

    for currRowIndex in range(rows):
        currRow = mat[currRowIndex]
        colsPtr = max_ones_col_index
        while colsPtr >= 0 and currRow[colsPtr] == 1:
            colsPtr -= 1

        if colsPtr < max_ones_col_index:
            max_ones_col_index = colsPtr
            resRowIndex = currRowIndex
    return resRowIndex


def findRow(mat):
    # APPROACH::
    # Ex_
    #  0 1 1 1
    #  0 0 1 1
    #  1 1 1 1    // this row has maximum 1s
    #  0 0 0 0

    # FOR EVERY ROW, ITERATE FROM LAST END COLUMN,
    # KEEP MOVING LEFTWARD TILL WE ENCOUNTER 1, ELSE MOVE TO NEXT ROW
    # NOW, MOVE TO NEXT ROW, NOW WE WILL START FROM COLUMN,
    # WHERE WE LEFT IN PREVIOUS ROW AND MOVE LEFTWARDS,
    # NOW IF IN THIS ROW WE STILL ENCOUNTERS 1 while moving leftwards
    # means we have more 1's then in previous row, so update our
    # max1sRow with this current row index.
    # Keep doing this and end we will get the required row.

    rows = len(mat)
    cols = len(mat[0])

    max1sRowIndex = 0
    index = cols - 1
    previouslyLeftColIndex = cols - 1
    # loop taking every rowIndex and row

    for currRowIndex, currRow in enumerate(mat):

        # iterate currRow form end till there are 1's
        while index >= 0 and currRow[index] == 1:
            index -= 1

        # if below,condition,means we have move more ,leftwards
        # compare to previous row,means more 1's in this row.
        if index < previouslyLeftColIndex:
            max1sRowIndex = currRowIndex
            previouslyLeftColIndex = index

    print('i', max1sRowIndex)

    return max1sRowIndex


# The time complexity is O(m+n)
def findRow1(mat):
    rows = len(mat)
    cols = len(mat[0])

    max1sRowIndex = 0
    index = cols - 1
    # loop for every row
    for i in range(rows):
        flag = False
        # if we enter this while loop means whe have more 1's then previous row
        while index >= 0 and mat[i][index] == 1:
            flag = True
            index = index - 1

            if flag:
                max1sRowIndex = i

        if max1sRowIndex == 0 and mat[0][cols - 1] == 0:
            return 0
    return max1sRowIndex


# 0 1 1 1
# 0 0 1 1
# 1 1 1 1  // this row has maximum 1s
# 0 0 0 0

mat = [
    [0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]
print(findRow(mat))
print(maxOneRow(mat))
