# Using Intersection of array technique
# O(n1 +n2 + n3)
# space O(1)
def findCommon(a1, a2, a3):
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j < len(a2) and k < len(a3):

        if a1[i] == a2[j] == a3[k]:
            print(a1[i])
            i = i + 1
            j = j + 1
            k = k + 1

        elif a1[i] < a2[j]:
            i = i + 1

        elif a2[j] < a3[k]:
            j = j + 1
        # We reach here when x > y and z < y, i.e., z is smallest
        else:
            k = k + 1


ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

findCommon(ar1, ar2, ar3)
