class Queue:

    def __init__(self):
        self.arr = []
        self.count = 0
        self.findex = 0

    # enqueue at O(1)____________________________________________________
    def enqueue(self, data):
        self.arr.append(data)
        self.count = self.count + 1

    # dequeue at O(1)____________________________________________________
    def dequeue(self):
        if self.count == 0:
            return -1
        elem = self.arr[self.findex]
        self.findex += 1
        self.count -= 1
        return elem

    # Size At O(1)___________________________________________________________
    def size(self):
        return self.count

    # Empty____________________________________________________________________
    def isEmpty(self):
        return self.size() == 0

    # front___________________________________________________________________
    def front(self):
        if self.count == 0:
            return -1
        return self.arr[self.findex]
