# this solution copy list and passes list[1:]
def sorted(list):
    if len(list)==1:
        return True
    if list[0]<list[1]:
        return sorted(list[1:])
    else:
        return False

#--Better Solution without copying list again and again passing
# as in above solution i.e list[1:]
def sortedBetter(list , i):
    l = len(list)
    if i==l-1 or l==0:
        return True

    if list[i]<list[i+1]:
        ans =  sortedBetter(list, i=i+1)
        return ans
    else:
        return False
list = input().split()
print(sorted(list))
print(sortedBetter(list , 0))
