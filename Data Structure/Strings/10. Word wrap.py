def getJustifiedLine(line, lineLength, maxWidth):
    numberOfSpaces = maxWidth - lineLength  # 5
    numberOfWords = len(line)  # 3

    if len(line) == 1:
        # if there is only word in line
        # just insert overall_spaces_count for the remainder of line
        return line[0] + ' ' * numberOfSpaces
    else:
        spaceGroups = numberOfWords - 1  # 2
        spacesBtwWords = numberOfSpaces // spaceGroups
        extraSpaces = numberOfSpaces % spaceGroups
        res = ''
        for word in line:
            space = ' ' * spacesBtwWords
            if extraSpaces > 0:
                space += ' '
                extraSpaces -= 1
            res += word + space
        return res


def fullJustify(words, maxWidth):
    lineLength = 0
    line = []
    answer = []

    for word in words:
        if lineLength + len(word) + len(line) <= maxWidth:
            # keep adding words until we can fill out maxWidth
            # width = sum of length of all words (without overall_spaces_count)
            # len(word) = length of current word
            # len(line) = number of overall_spaces_count to insert between words
            lineLength += len(word)
            line.append(word)
        else:
            # justify the line and add it to result
            justifiedLine = getJustifiedLine(line, lineLength, maxWidth)
            answer.append(justifiedLine)
            # reset new line and new width
            line = [word]
            lineLength = len(word)

    # last line
    number_spaces = maxWidth - lineLength
    last_line1 = ' '.join(line) + (number_spaces * ' ')
    answer.append(last_line1)
    return answer


# what must be acknowledgment shall be
# 15
# words = [i for i in input().strip().split()]
words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
         "is", "everything", "else", "we", "do"]
maxWidth = int(input())
ans = fullJustify(words, maxWidth)
for x in ans:
    print(x)
