def printHelperRecursive(wordList, curr_row, curr_col, output):
    # 1. append curr word of row to output to form a sentence
    output[curr_row] = wordList[curr_row][curr_col]

    # 2. if wordList end of row is reached, we will print sentence so,formed
    if curr_row == len(wordList) - 1:
        for i in range(len(wordList)):
            print(output[i], end=' ')
        print()
        return

    # 3. recur for next word in next row to form sentence
    for j in range(len(wordList[0])):

        if wordList[curr_row + 1][j] != '':
            printHelperRecursive(wordList, curr_row + 1, j, output)


def printSentences(wordList):
    mRows = len(wordList)
    nCols = len(wordList[0])

    # for every word in first list ,we will form a sentence
    for i in range(nCols):
        # output arr to store words of sentence
        output = [''] * mRows

        if wordList[0][i] != '':
            printHelperRecursive(wordList, 0, i, output)


arr = [["you", "we", ""],
       ["have", "are", ""],
       ["sleep", "eat", "drink"]]
printSentences(arr)
