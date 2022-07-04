# Input : a = 10, b = 20
# Output : 4
# Binary representation of a is 00001010
# Binary representation of b is 00010100
# We need to flip highlighted four bits in a
# to make it b.
#
# Input : a = 7, b = 10
# Output : 3
# Binary representation of a is 00000111
# Binary representation of b is 00001010
# We need to flip highlighted three bits in a
# to make it b.


# T: O(LogN)
def convertAtoB(a, b):
    def countFlips(a, b):
        # O(1)
        n = a ^ b

        # O(logN)
        count = 0
        while n:
            n = n & (n - 1)  # Important step, count set bits in number
            count += 1
        return count

    return countFlips(a, b)


A = 10
B = 20
ans = convertAtoB(A, B)
print(ans)
