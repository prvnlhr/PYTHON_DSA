import queue


class Stack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x):
        self.stack.append(x)
        self.size = self.size + 1

    def pop(self):

        if self.isEmpty():
            return
        self.stack.pop()
        self.size = self.size - 1

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[-1]

    def isEmpty(self):
        return self.size == 0

    def length(self):
        return self.size


stackObj = Stack()
stackObj.push(2)
stackObj.push(3)
stackObj.push(-1)
stackObj.push(5)
print(stackObj.stack)
stackObj.pop()
print(stackObj.stack)
print(stackObj.isEmpty())
print(stackObj.length())
