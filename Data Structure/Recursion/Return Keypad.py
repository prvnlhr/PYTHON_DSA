def getString(ld):
    if ld == 2:
        return "abc"
    if ld == 3:
        return "def"
    if ld == 4:
        return "ghi"
    if ld == 5:
        return "jkl"
    if ld == 6:
        return "mno"
    if ld == 7:
        return "pqrs"
    if ld == 8:
        return "tuv"
    if ld == 9:
        return "wxyz"
    return ""


def keypad(n):
    if n == 0:
        output = []
        output.append("")
        return output

    smallnumber = n // 10
    ld = n % 10

    smalleroutput = keypad(smallnumber)
    optionsforLD = getString(ld)

    output = []
    for s in smalleroutput:
        for c in optionsforLD:
            option = s + c
            output.append(option)
    return output


def PrintKeypad(n, outputSoFar):
    if n == 0:
        print(outputSoFar)
        return

    smallnumber = n // 10
    ld = n % 10

    optionsforLD = getString(ld)

    for c in optionsforLD:
        newOutput = c + outputSoFar
        PrintKeypad(smallnumber, newOutput)


n = int(input())
ans = keypad(n)
for s in ans:
    print(s)
