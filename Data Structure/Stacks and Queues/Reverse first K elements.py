from sys import stdin
import queue


# reverseKElements function:___________________________

def reverseKElements(inputQueue, k):
    if (inputQueue.empty() or (k > inputQueue.qsize())):
        return inputQueue

    if k <= 0:
        return inputQueue

    stack = list()

    for i in range(k):
        stack.append(inputQueue.get())

    while not isEmpty(stack):
        inputQueue.put((stack.pop()))

    for i in range(inputQueue.qsize() - k):
        inputQueue.put(inputQueue.get())

    return inputQueue


# Utility function:_____________________________________
def isEmpty(stack):
    return len(stack) == 0


def top(stack):
    return stack[len(stack) - 1]


def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n):
        qu.put(values[i])
    return k, qu


k, q = takeInput()
qu = reverseKElements(q, k)

while not qu.empty():
    print(qu.get(), end=" ")
