def permutations( s):
    printPermu(s , "")

def printPermu(s , output):

    if len(s) ==0:
        print(output)
        return
    for i in range( 0 , len(s)):
        printPermu(s[0:i] + s[i+1:] , output + s[i])

s = input()
permutations(s)




