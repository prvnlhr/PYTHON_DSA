
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class QueueUsingLL:

    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def enqueue(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.count = self.count + 1



    def dequeue(self):
        if self.head is None:
            return -1
        elem = self.head.data
        self.head = self.head.next
        self.count = self.count - 1
        return elem


    def front(self):
        if self.head is None:
            return -1
        elem = self.head.data
        return elem


    def isEmpty(self):
        return self.getSize()==0

    def getSize(self):
        return self.count


q = QueueUsingLL()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        q.enqueue(li[i+1])
        i+=1
    elif choice == 2:
        ans = q.dequeue()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = q.front()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(q.getSize())
    elif choice == 5:
        if(q.isEmpty()):
            print('true')
        else:
            print('false')
    i+=1







