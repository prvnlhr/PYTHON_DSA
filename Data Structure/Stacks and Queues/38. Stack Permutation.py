import queue


# Given two arrays, both of unique elements. One represents
# the input queue and the other represents the output queue.
# Our task is to check if the given output is possible through
# stack permutation.

# Input : First array: 1, 2, 3
#         Second array: 2, 1, 3
# Output : Yes

# Procedure:
# push 1 from input to stack
# push 2 from input to stack
# pop 2 from stack to output
# pop 1 from stack to output
# push 3 from input to stack
# pop 3 from stack to output
#
#
# Input : First array: 1, 2, 3
#         Second array: 3, 1, 2
# Output : Not Possible

# SELF SOLVED 100% CN solution__
# code studio optimised__
def findPermutation1(arr1, arr2):
    stack = []
    arr1_ptr = 0
    arr2_ptr = 0
    while arr1_ptr < len(arr1):
        ele = arr1[arr1_ptr]
        stack.append(arr1[arr1_ptr])
        while stack and arr2[arr2_ptr] == stack[-1]:
            stack.pop()
            arr2_ptr += 1
        arr1_ptr = arr1_ptr + 1

    if len(stack) == 0:
        return 'YES'


def findPermutation(arr1, arr2):
    # create two queues
    # from arr1 and arr2 elements
    # arr1 -> inputQueue
    # arr2 -> outputQueue

    inputQueue = queue.Queue()
    for val in arr1:
        inputQueue.put(val)

    outputQueue = queue.Queue()
    for val in arr2:
        outputQueue.put(val)

    # maintain a stack
    stack = []

    # Loop till inputQueue does not become zero
    while not inputQueue.empty():

        # get queue top ele
        ele = inputQueue.queue[0]
        inputQueue.get()

        # if inputQueue top == outputQueue top
        if ele == outputQueue.queue[0]:
            outputQueue.get()
            # if equal then pop stack till stack_top == outputQueue top
            while stack:
                if stack[-1] == outputQueue.queue[0]:
                    stack.pop()
                    outputQueue.get()
                else:
                    break
        # else inputQueue top != outputQueue top
        else:
            stack.append(ele)

    # at end if length of stack is  and inputQueue is empty ,
    # we have stack permutation
    final_length_of_stack = len(stack)
    is_InputQueue_empty = inputQueue.empty()
    return final_length_of_stack == 0 and is_InputQueue_empty


# SAME AS ABOVE BUT MADE MORE READABLE___
# NOTE:: This solution is optimised but not more then first CN solution
def permutation(arr1, arr2):
    inputQueue = queue.Queue()
    for val in arr1:
        inputQueue.put(val)

    outputQueue = queue.Queue()

    for val in arr2:
        outputQueue.put(val)
    stack = []
    while not inputQueue.empty():
        ele = inputQueue.get()
        stack.append(ele)
        while stack and outputQueue.queue[0] == stack[-1]:
            outputQueue.get()
            stack.pop()
    if len(stack) == 0 and inputQueue.empty():
        return 'YES'


# arr1 = [int(i) for i in input().strip().split()]
# arr2 = [int(j) for j in input().strip().split()]
# 2
# 3
# 2 4 6
# 4 6 2
# 3
# 2 4 6
# 6 2 4
T = int(input())
while T > 0:
    n = int(input())
    arr1 = [int(i) for i in input().strip().split()]
    arr2 = [int(j) for j in input().strip().split()]
    ans = findPermutation1(arr1, arr2)
    print(ans)
    T -= 1

# ans = findPermutation1(arr1, arr2)
# print(ans)
