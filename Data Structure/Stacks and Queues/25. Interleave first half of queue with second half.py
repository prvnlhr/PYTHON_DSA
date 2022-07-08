import queue


# Ex_.
# 11 12 13 14 15 16 17 18 19 20
# 11 16 12 17 13 18 14 19 15 20

# TRICK TO REMEMBER::
# " WE ALWAYS NEED FIRST HALF ELEMENTS OF INPUT QUEUE IN STACK IN REVERSE ORDER "

# SO AT END WE WILL HAVE QUEUE's FIRST HALF's REVERSE IN STACK AND REST HALF IN QUEUE
# AND THEN WE CAN INTERLEAVE STACK AND QUEUE ELEMENTS.
def interleave(q):
    n = q.qsize()
    halfLength = n // 2
    stack = []

    # 1. put first  half element of queue to stack
    for i in range(halfLength):
        ele = q.get()
        stack.append(ele)

    # 2. put stack elements back to queue
    while stack:
        q.put(stack[-1])
        stack.pop()

    # 3. remove first half elements and put them to queue back
    for j in range(halfLength):
        ele = q.get()
        q.put(ele)

    # 4. Again put first half elements of queue to stack
    for l in range(halfLength):
        ele = q.get()
        stack.append(ele)

    # 5. Interleave q and stack elements
    while stack:
        ele1 = stack.pop()
        q.put(ele1)
        ele2 = q.get()
        q.put(ele2)
    return q


arr = [int(i) for i in input().strip().split()]
q = queue.Queue()
for ele in arr:
    q.put(ele)

ans = interleave(q)
while q.empty() == False:
    print(q.get(), end=' ')
