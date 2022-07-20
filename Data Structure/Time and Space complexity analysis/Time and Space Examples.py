def findPair(a, n, z):
    # Iterate through all the pairs
    for i in range(n):  # N times
        for j in range(n):  # N times

            # Check if the sum of the pair
            # (a[i], a[j]) is equal to z
            if (i != j and a[i] + a[j] == z):
                return True
    return False

# TIME :
# O(N * N)

# ___________________________________________________________________________________________________________-
# N = 8
# int count = 0 ;
# for (int i = N; i > 0; i /= 2)
#     for (int j = 0; j < i; j++)
#         count++;

# AT first time complexity seems to be logN for outer i loop , and N for inner j loop,but it is wrong

# N = 8 ,
# First iteration i = 8 , j = i = 8 , so count runs for 8 times.  ->  N
# Second iteration i /= 2 = 4  , j = i = 4 , so count runs for 4 times. -> N/2
# Third iteration i /= 2 = 2  , j = i = 2 , so count runs for 2 times. -> N / 4
# and so ....

# SO in worst case time complexity will be 8 ,which is for first iteration ,which is equal to N
# T :    N + N/2 + N/4 ..  =    O(N)
