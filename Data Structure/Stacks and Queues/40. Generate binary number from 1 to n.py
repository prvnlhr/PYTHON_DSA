import queue


def generate(n):
    q = queue.Queue()
    q.put('1')

    for i in range(n):
        front = q.get()
        q.put(front + '0')
        q.put(front + '1')
        print(front, end=' ')


n = int(input())
generate(n)
