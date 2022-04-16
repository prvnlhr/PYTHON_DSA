# Given an n x n binary matrix image, flip the image
# horizontally, then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the
# image is reversed. For example, flipping[1, 1, 0] horizontally
# results in [0, 1, 1]. To invert an image means that each 0 is
# replaced by 1, and each 1 is replaced by 0.
# For example, inverting[0, 1, 1] results in [1, 0, 0].

# Example 1:
#
# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:
#
# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]


# AFTER LOOKING CAREFULLY,
# WE NOTICED THAT, IF element at i and j are different , i.e means after reversing and reverting
# they will become same as original. so if ele at i == ele at j ,do nothing
# But if both ele are same then after reversing and reverting they become opposite of original
# so simple make then opposite. this way we are not reversing and reverting
# This is my intuition but there may be multiple possibilities


# O(N) , single pass
# Self solved 100% leetcode
def rotateImageOPT(image):
    for row in image:
        i = 0
        j = len(row) - 1

        while i <= j:
            if i == j:  # this condition is for middle col when i == j
                #         eliminates the loop to change middle col elements

                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0
                break

            else:
                if row[i] == row[j]:
                    if row[i] == 0:
                        row[i] = 1
                    else:
                        row[i] = 0
                    if row[j] == 0:
                        row[j] = 1
                    else:
                        row[j] = 0
                i += 1
                j -= 1

    return image


# Self solved 100% leetcode
# O(N), Two pass
def rotateImage(image):
    # O(N)
    for row in image:
        i = 0
        j = len(row) - 1
        while i < j:
            if row[i] == row[j]:
                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0
                if row[j] == 0:
                    row[j] = 1
                else:
                    row[j] = 0
            i += 1
            j -= 1

    # O(N)
    if len(image[0]) % 2 != 0:
        midIndex = len(image[0]) // 2
        r = 0
        while r < len(image):
            if image[r][midIndex] == 1:
                image[r][midIndex] = 0
            else:
                image[r][midIndex] = 1
            r += 1

    return image


# image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
# image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
# image = [[1]]
# image = [[0, 1, 1, 1, 1], [0, 1, 1, 0, 0], [0, 1, 1, 1, 1], [1, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
image = [[1, 1, 0, 1, 1], [0, 0, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 1], [0, 1, 1, 0, 0]]
ans = rotateImage(image)
# print([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]])
# print([[1, 0, 0], [0, 1, 0], [1, 1, 1]])
# print('expected', [[0, 0, 1, 0, 0], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [0, 0, 0, 0, 1], [1, 1, 0, 0, 1]])
print('q', [[1, 1, 0, 1, 1], [0, 0, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 1], [0, 1, 1, 0, 0]])
print('e', [[0, 0, 1, 0, 0], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [0, 0, 0, 0, 1], [1, 1, 0, 0, 1]])
for row in ans:
    print(row)
