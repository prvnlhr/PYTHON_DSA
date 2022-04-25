# Ex_1.
# 1.2.4
# 1.2.3
# -> 1

# Ex_2.
# 10.2.2
# 10.2.2
# -> 0

# Ex_3.
# 123.45
# 123
# -> 1

# Ex_4.
# 1.0.0
# 1
# -> 0

# Approach: It is not possible to compare them directly because
# of the dot, but the versions can compare numeric part wise
# and then the latest version can be found. Traverse through
# strings and separate numeric parts and compare them. If equal,
# then the next numeric part is compared and so on until they 
# differ, otherwise flag them as equal.
# Implement a method to compare the two versions. If there
# are more than two versions, then the below versionCompare
# method can be used as a compare method of sort method, which
# will sort all versions according to the specified comparison.

def compareVersions(a, b):
    # 1. Split the strings on basis of the dot '.'
    arr1 = a.split('.')
    arr2 = b.split('.')
    m = len(arr1)
    n = len(arr2)
    # 2. convert string in array to int
    arr1 = [int(i) for i in arr1]
    arr2 = [int(i) for i in arr2]

    # 3. check if both string are of same length
    # if there are not same length then we
    # need to put zero's to the shorted string to
    # make them of equal length
    if m > n:
        x = m - n
        for i in range(x):
            arr2.append(0)

    elif n > m:
        x = n - m
        for j in range(x):
            arr1.append(0)

    # 4. compare numbers one by one.
    for num1, num2 in zip(arr1, arr2):
        if num1 > num2:
            return 1
        elif num2 > num1:
            return -1
    return 0


a = '1.20.405'
b = '1.20.404'
ans = compareVersions(a, b)
# ans = compare(a, b)
print(ans)
