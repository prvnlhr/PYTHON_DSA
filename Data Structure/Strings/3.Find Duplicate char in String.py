def findDuplicate(s):
    m = {}

    for i in range(len(s)):
        ele = s[i]
        if ele in m:
            m[ele] = m[ele] + 1
            print(ele, end=' ')
        else:
            m[ele] = 1


s = input()
findDuplicate(s)
