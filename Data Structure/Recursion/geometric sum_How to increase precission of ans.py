# import math
# import decimal
# def GeoSum(k):
#     if (k == 0):
#         return 1
#
#     return GeoSum(k - 1) + 1 / math.pow(2,k)
#
#
# k = int(input())
# ans = decimal.Decimal(GeoSum(k))
# print(ans)
import math
import decimal
# from decimal import *
# getcontext().prec = 10 #Since you want the 5 level of precision

def GeoSum(k):
    if (k == 0):
        return 1

    return GeoSum(k - 1) + 1 / (math.pow(2,k))


k = int(input())
ans = (GeoSum(k))
#If you want to print the trailing zeros as well. Then do as following
print('{:.4f}'.format(ans))
print(ans)
