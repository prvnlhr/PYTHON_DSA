# O(n) space
def reverseString(s):
    ans = ''
    for i in range(len(s) - 1, -1, -1):
        ans = ans + s[i]

    print(ans)


# IF STRING IS REPRESENTED AS ARRAY OF CHARACTER SOL 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# ELSE SOL 2:
# s = hello
# _______________________________________________________________________________________________________________
# SOL 1:
def reverseString(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        j = j - 1
    return arr


# ________________________________________________________________________________________________________________
# SOL 2:
# applying recursion :
# taking 0'th string Char and appending to last and
# then slicing , excluding 1st char from string

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


# arr = [i for i in input().strip().split()]
s = 'hello'
# ans = reverseString((arr))
ans = reverse(s)
print(ans)

s = input()
reverseString(s)
