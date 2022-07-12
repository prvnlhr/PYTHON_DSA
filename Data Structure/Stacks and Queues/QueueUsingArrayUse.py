from QueueUsingArray import Queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print("size", q.count)
while (q.isEmpty() is False):
    print(q.front())
    q.dequeue()
print("Size", q.count)
print(q.dequeue())
