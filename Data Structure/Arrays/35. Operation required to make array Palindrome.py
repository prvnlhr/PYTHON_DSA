# Ex__1. 6 1 4 3 1 7

# Steps:
#     6 1 4 3 1 7
#     |         |
#     i         j
# if arr[i] == arr[j],  i++ , j--
# if arr[i] < arr[j],   arr[i+1] = arr[i+1] + arr[i] , i++, merge
# if arr[i] > arr[j],   arr[j - 1] = arr[j - 1] + arr[j] , j-- , merge
# __Dry run :___________________________________________________________________________________________

#  ex_ 6 1 4 3 1 7

#  i         j   if arr[i] < arr[j] -> merge arr[i+1] = arr[i] + arr[i+1]
#  6 1 4 3 1 7 -->    { 6 , 1 } , 4 , 3 , 1 , 7
#  |<-diff-> |            |
#                         7 , 4 , 3 , 1 , 7
#                         |    <-same->   |

#           i         j  if arr[i] > arr[j] -> merge arr[j-1] = arr[j] + arr[j-1]
#       7 , 4 ,  3 ,  1 ,7       7 , 4 , {3 , 1} , 7       7 , 4 , 4 , 7
#           |<-diff->|               |       |

#  7, 4 , 4 , 7 --> palindrome
# now array became palindrome

# STEPS::
# 6 1 4 3 1 7 --> [6, 7, 4, 3, 1, 7]
# [6, 7, 4, 3, 1, 7] --> [6, 7, 4, 3, 1, 7]
# [6, 7, 4, 3, 1, 7] --> [6, 7, 4, 4, 1, 7]
# [6, 7, 4, 4, 1, 7]

def makeArrayPalindrome(arr):
    i = 0
    j = len(arr) - 1
    count_of_operation = 0
    while i < j:
        if arr[i] == arr[j]:
            i = i + 1
            j = j - 1
        elif arr[i] < arr[j]:
            arr[i + 1] = arr[i + 1] + arr[i]
            i = i + 1
            count_of_operation = count_of_operation + 1

        elif arr[i] > arr[j]:
            arr[j - 1] = arr[j - 1] + arr[j]
            j = j - 1
            count_of_operation = count_of_operation + 1

    return count_of_operation


arr = [int(i) for i in input().strip().split()]
ans = makeArrayPalindrome(arr)

print(ans)
