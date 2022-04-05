#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.


# def minimumBribes(q):
# def minimumBribes(Q):
#     #
#     # initialize the number of moves
#     moves = 0
#     #
#     # decrease Q by 1 to make index-matching more intuitive
#     # so that our values go from 0 to N-1, just like our
#     # indices.  (Not necessary but makes it easier to
#     # understand.)
#     Q = [P - 1 for P in Q]
#     #
#     # Loop through each person (P) in the queue (Q)
#     for i, P in enumerate(Q):
#         # i is the current position of P, while P is the
#         # original position of P.
#         #
#         # First check if any P is more than two ahead of
#         # its original position
#         if P - i > 2:
#             print("Too chaotic")
#             return
#         #
#         # From here on out, we don't care if P has moved
#         # forwards, it is better to count how many times
#         # P has RECEIVED a bribe, by looking at who is
#         # ahead of P.  P's original position is the value
#         # of P.
#         # Anyone who bribed P cannot get to higher than
#         # one position in front if P's original position,
#         # so we need to look from one position in front
#         # of P's original position to one in front of P's
#         # current position, and see how many of those
#         # positions in Q contain a number large than P.
#         # In other words we will look from P-1 to i-1,
#         # which in Python is range(P-1,i-1+1), or simply
#         # range(P-1,i).  To make sure we don't try an
#         # index less than zero, replace P-1 with
#         # max(P-1,0)
#         for j in range(max(P - 1, 0), i):
#             if Q[j] > P:
#                 moves += 1
#     print(moves)
#     # Solution 2 :
#     # n is the number of people in the list
#     # q is the order of the people after the bribery has taken place ex. [1, 3, 2, 5, 4]
#     #     n = len(Q)
#     n = len(Q)
#     for I in range(1, n + 1):  # for each person I in the list
#         index = q.index(I)
#         if I - index > 3:  # more than two bribes
#             bribes = "Too chaotic"
#             break
#         for j in range(index):  # for each number to the left of I, if greater than I, count it as a bribe
#             if q[j] > I:
#                 bribes = bribes + 1
#     print(bribes)
#

# OPTIMISED______________
def minimumBribes(q):
    count = 0
    tooChaotic = False

    for i in range(len(q)):

        # to translate between q[i] and the position in a zero-indexed python
        # list, you have to add 1, so here it's i+3 rather than i+2

        if q[i] > i + 3:
            print("Too chaotic")
            tooChaotic = True
            break
        else:

            # q[i]-2 rather than q[i]-1 since python is zero-indexed
            # but the people in the queue start at 1

            start = max(0, q[i] - 2)
            for j in range(start, i):
                if q[j] > q[i]:
                    count += 1

    if tooChaotic == False:
        print(count)


# if __name__ == '__main__':
#     t = int(input())
#
#     for t_itr in range(t):
#         n = int(input())
#
#         q = list(map(int, input().rstrip().split()))
#
#         minimumBribes(q)

def minimumBribe(Q):
    moves = 0
    n = len(Q)
    P = [int(i) for i in range(1, n + 1)]
    # print(Q)
    # print(P)
    # print()
    res = 0
    for i in range(n - 1, -1, -1):

        if Q[i] == P[i]:
            if moves >= 3:
                return 'To chaotic'

        if Q[i] < P[i]:
            P[i], P[i - 1] = P[i - 1], P[i]
            # print(P)
            moves += 1
    # print()
    # print(Q)
    # print(P)
    return moves


testCases = [[2, 1, 5, 3, 4], [2, 5, 1, 3, 4], [1, 2, 3, 5, 4, 6, 7, 8], [4, 1, 2, 3]]
for test in testCases:
    ans = minimumBribe(test)
    print(ans)
