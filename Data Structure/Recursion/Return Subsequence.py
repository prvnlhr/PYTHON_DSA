def subsequences(string):
    if len(string) == 0:
        output = []
        output.append("")
        return output
    smalleroutput = subsequences(string[1:])

    output = []
    for sub in smalleroutput:
        output.append(sub)

    for sub in smalleroutput:
        subs_with_zeroth_char = string[0] + sub
        output.append(subs_with_zeroth_char)
    return output


# OR CN SOLUTION
def subsequencesCN(string):
    if len(string) == 0:
        output = []
        output.append("")
        return output
    smalleroutput = subsequences(string[1:])

    output = []
    for sub in smalleroutput:
        output.append(sub)
        output.append(string[0] + sub)
    return output


def PrintsubsequencesCN(string, outputSoFar):
    if len(string) == 0:
        print(outputSoFar)
        return

    PrintsubsequencesCN(string[1:], outputSoFar)
    newOutput = outputSoFar + string[0]
    PrintsubsequencesCN(string[1:], newOutput)


string = input()
ans = subsequencesCN(string)
for ele in ans:
    print(ele)
