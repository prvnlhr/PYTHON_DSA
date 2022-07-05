import sys


class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.Min = sys.maxsize

    # ________________________________________________

    def printStack(self):
        print(self.stack)

    # ________________________________________________

    def push(self, x):
        # When we are push a element in stack ,we are also ,
        # storing a min value util that element --> [(x,Min),[(,)],[(,)]...]

        self.Min = min(x, self.Min)
        # Here we append a tuple in stack not a single element [(,)]
        self.stack.append((x, self.Min))
        self.size = self.size + 1

    # As we are storing pair in stack,
    # after popping a element from stack,
    # there may be two conditions,
    # if stack becomes empty --> we reset self.Min value to maxsize
    # else --> self.Min will be last element in Stack pair
    # ________________________________________________

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

    # ________________________________________________

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[-1][0]

    # ________________________________________________

    def getMin(self):

        if self.size == 0:
            return None
        return self.stack[-1][1]

    # ________________________________________________
    def isEmpty(self):
        return self.size == 0

    # ________________________________________________

    def getSize(self):
        return self.size
    # ________________________________________________


minStack = MinStack()
minStack.push(-10)
minStack.push(14)
print(minStack.printStack())
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
