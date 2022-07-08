import queue

q = queue.Queue()


def reverseQueue(q):
    if q.empty() == True:
        return q
    ele = q.get()
    q = reverseQueue(q)
    q.put(ele)
    return q


arr = [int(i) for i in input().strip().split()]
for ele in arr:
    q.put(ele)
ans = reverseQueue(q)
while ans.empty() == False:
    print(ans.get(), end=' ')
