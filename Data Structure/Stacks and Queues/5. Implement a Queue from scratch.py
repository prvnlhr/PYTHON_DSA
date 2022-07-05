# Using Array Data Structure
class Queue:

    def __init__(self):
        self.array = []
        self.size = 0
        self.frontIndex = 0

    def Enqueue(self, x):
        self.array.append(x)
        self.size = self.size + 1

    def Dequeue(self):
        if self.isEmpty():
            return
        else:
            # trick is to maintain a frontIndex,
            ele = self.array[self.frontIndex]
            self.frontIndex = self.frontIndex + 1
            self.size = self.size - 1

    def front(self):
        if self.isEmpty():
            return None
        else:
            return self.array[self.frontIndex]

    def isEmpty(self):
        return self.size == 0

    def Size(self):
        return self.size


queue = Queue()
queue.Enqueue(1)
queue.Enqueue(2)
queue.Enqueue(3)
queue.Enqueue(4)
print(queue.array)
print(queue.front())

queue.Dequeue()
print(queue.front())
print(queue.array)

print(queue.isEmpty())
print(queue.Size())
