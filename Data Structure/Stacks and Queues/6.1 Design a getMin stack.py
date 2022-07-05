import sys


class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.Min = sys.maxsize

    def push(self, x):

        self.Min = min(x, self.Min)
        self.stack.append((x, self.Min))
        self.size = self.size + 1

    def pop(self):
        if self.isEmpty():
            return
        else:
            self.stack.pop()
            self.size = self.size - 1
        if len(self.stack) == 0:
            self.Min = sys.maxsize
        else:
            self.Min = self.stack[-1][1]
        self.size = self.size - 1

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[-1][0]

    def getMin(self):
        if self.size == 0:
            return None
        return self.stack[-1][1]

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size


minStack = MinStack()
minStack.push(-10)
minStack.push(14)
print('min', minStack.getMin())
print('min', minStack.getMin())
minStack.push(-20)
print('min', minStack.getMin())
print('min', minStack.getMin())
print('top', minStack.top())
print('min', minStack.getMin())
minStack.pop()
minStack.push(10)
minStack.push(-7)
print('min', minStack.getMin())
minStack.push(-7)
minStack.pop()
print('top', minStack.top())
print('min', minStack.getMin())
minStack.pop()
