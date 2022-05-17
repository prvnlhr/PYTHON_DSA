#           Ex 1_:
#                     1
#                   /   \
#                  2     5
#                 / \     \
#                3   4     6
#
#           Output:
#               1
#                \
#                 2
#                  \
#                   3
#                    \
#                     4
#                      \
#                       5
#                        \
#                         6
#
#           Ex_2:
#                   1
#                  / \
#                 3   4
#                    /
#                   2
#                    \
#                     5
#           Output:
#                1
#                 \
#                  3
#                   \
#                    4
#                     \
#                      2
#                       \
#                        5

import BinaryTreeInputPrint


def flattenBt(root):
    if root is None:
        return

    flattenBt(root.left)
    flattenBt(root.right)

    #                     1
    #                   /   \
    #       root ->    2     5
    #                 / \     \
    #                3   4     6

    left = root.left  # left = root.left -> 3
    right = root.right  # right = root.right -> 4

    root.left = None
    root.right = left

    #                     1
    #                   /   \
    #       root ->    2     5
    #                 / \     \
    #              None  3     6
    #
    temp = root
    while temp.right:
        temp = temp.right
    temp.right = right

    #                       1
    #                   /       \
    #       root ->    2 <-temp  5
    #                 / \          \
    #              None  3 <-temp   6
    #                        \
    #                         4 <-right


#

#
BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
flattenBt(root)
BT.PrintLevelWise(root)
