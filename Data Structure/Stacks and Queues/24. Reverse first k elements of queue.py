# Input : Q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#         k = 5
# Output : Q = [50, 40, 30, 20, 10, 60, 70, 80, 90, 100]

# Create an empty stack.
# One by one dequeue first K items from given queue and push
# the dequeued items to stack.
# Enqueue the contents of stack at the back of the queue
# Dequeue (size-k) elements from the front and enqueue them one by
# one to the same queue.
#
#
import queue


def reverseKelements(q, k):
    stack = []
    for i in range(k):
        stack.append(q.queue[0])
        q.get()

    while stack:
        x = stack.pop()
        q.put(x)

    for j in range(len(arr) - k):
        ele = q.queue[0]
        q.get()
        q.put(ele)
    return q


k = int(input())
arr = [int(i) for i in input().strip().split()]
q = queue.Queue()
for ele in arr:
    q.put(ele)
ans = reverseKelements(q, k)
while not ans.empty():
    print(ans.get(), end=' ')
