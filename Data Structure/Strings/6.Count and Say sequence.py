# Example 1:
#
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.
# Example 2:
#
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"


def countAndSay(n):
    # ___GeeksForGeeks solution
    # if n == 1:
    #     return '1'
    # if n == 2:
    #     return '11'
    #
    # s = '11'
    #
    # for i in range(3, n + 1):
    #     s = s + '$'
    #     l = len(s)
    #
    #     count = 1
    #     temp = ''
    #     for j in range(1, l):
    #
    #         if (s[j] != s[j - 1]):
    #             temp = temp + str(count + 0)
    #             temp = temp + s[j - 1]
    #             count = 1
    #         else:
    #             count = count + 1
    #
    #     s = temp
    # return s

    # _self solved after too much thinking:
    # INTUITION::
    # 1. recurse and get ans for n == 1 ,and return it which will get saved as s
    if n == 1:
        return '1'

    s = countAndSay(n - 1)
    # 2. now we got ans for n == 1 , s = '1'

    # Initialize variable ,
    count = 1
    # empty string
    temp = ''
    # iterator for iterating s
    i = 1
    # starting from index i == 1 to  len(s)+1
    # ex._  we got s == '21'
    #         2 1
    #           |
    #           i
    # compare ith and i-1th char, 1 and 2 , if equal count +=1
    # else not equal create temp string
    # finally return temp
    print(s)
    while i < len(s) + 1:
        # print(temp)
        if i < len(s) and s[i] == s[i - 1]:
            count = count + 1
        else:
            temp = temp + str(count) + str(s[i - 1])
            count = 1
        i = i + 1
    return temp


n = int(input())
ans = countAndSay(n)
print(ans)
