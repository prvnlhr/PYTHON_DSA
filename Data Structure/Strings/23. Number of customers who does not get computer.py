# 2, “ABBAJJKZKZ” should return 0
# 3, “GACCBDBDAGEE” should return 1 as ‘D’ was not able to get any computer
# 3, “GACCBGDDBAEE” should return 0
# 1, “ABCBCA” should return 2 as ‘B’ and ‘C’ were not able to get any computer.
# 1, “ABCBCADEED” should return 3

from collections import defaultdict


# SELF SOLVED PASSES 100% test cases
def countCustomers1(arr, k):
    map = defaultdict()
    count = 0
    for char in arr:
        # CASE 1:: CHAR ALREADY IN MAP(means we have encountered a char(person) when he is leaving the cafe
        # if char is already in map means,there are two possible conditions
        # 1. if char has been already assigned a computer --> if computer was assigned, means now as he is leaving
        #                                                     we can  increase computer count(k) as it will become free
        # 2. if no computer was assigned to char -> means on leaving this char, he has not got any computer,so
        #                                           we will increase count of not assigned
        if char in map:
            if map[char] == 0:
                count = count + 1

            elif map[char] == 1:
                k = k + 1
        # CASE 2:: IF CHAR NOT IN MAP( means we have encountered a char(person) first time,means he enter the cafe
        # if a char enter the cafe, means there are two possible conditions
        # 1. if we have available computer ,we will assigned to him in and add to map
        # 2. if no computer is available , we will add to map and assigned 0 computer to him
        elif char not in map:
            if k > 0:
                map[char] = 1
                k = k - 1
            elif k == 0:
                map[char] = 0
    return count


# SELF SOLVED PASSES 100% test cases
def countCustomers(avail_comp, seq):
    map = defaultdict()
    count = 0

    for char in seq:

        if char in map:
            if map[char] == 0:
                count = count + 1
            elif map[char] == 1:
                avail_comp = avail_comp + 1

        elif char not in map:
            if avail_comp > 0:
                map[char] = 1
                avail_comp = avail_comp - 1
            elif avail_comp == 0:
                map[char] = 0

    return count


# n = int(input())
# seq = input()

# gfg input
input = [[2, 'ABBAJJKZKZ'], [3, 'GACCBDDBAGEE'], [3, 'GACCBGDDBAEE'], [1, 'ABCBCA'], [1, 'ABCBCADEED']]

# CN input
input = [[2, [1, 2, 2, 1]], [2, [1, 3, 2, 1, 2, 3]]]

for obj in input:
    n = obj[0]
    seq = obj[1]
    print(n, seq)
    # ans = countCustomers(n, seq)
    ans = countCustomers1(seq, n)
    print(ans)
