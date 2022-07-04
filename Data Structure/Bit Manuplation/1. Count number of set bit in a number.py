# Input : n = 6
# Output : 2
# Binary representation of 6 is 110 and has 2 set bits
#
# Input : n = 13
# Output : 3
# Binary representation of 13 is 1101 and has 3 set bits


# Time Complexity: O(logN)

def countSetBits(num):
    count = 0
    while num:
        num = num & (num - 1)  # Important step, count set bits in number
        count += 1
    return count


number = int(input())
ans = countSetBits(number)
print(ans)
