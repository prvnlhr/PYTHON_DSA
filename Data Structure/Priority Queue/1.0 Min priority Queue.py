class PriorityQueueNode:
    def __init__(self, ele, priority):
        self.ele = ele
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        return self.getSize() == 0

    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele

    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex - 1) // 2

            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex], self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self, ele, priority):
        pqNode = PriorityQueueNode(ele, priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    # SELF WRITTEN DOWN HEAPIFY CODE 100%
    def downheapify(self):

        parentIndex = 0

        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 2

        while rightChildIndex < self.getSize() - 1:
            minIndex = parentIndex
            if self.pq[parentIndex].priority > (self.pq[leftChildIndex].priority or self.pq[rightChildIndex].priority):

                if self.pq[leftChildIndex].priority < self.pq[rightChildIndex].priority:
                    minIndex = leftChildIndex
                else:
                    minIndex = rightChildIndex

                # swap
                self.pq[parentIndex], self.pq[minIndex] = self.pq[minIndex], self.pq[parentIndex]
                parentIndex = minIndex
                leftChildIndex = 2 * parentIndex + 1
                rightChildIndex = 2 * parentIndex + 2

            else:
                break

    # CN DOWN HEAPIFY
    def downheapifyCN(self):
        parentIndex = 0
        leftIndex = 2 * parentIndex + 1
        rightIndex = 2 * parentIndex + 2

        while leftIndex < (self.getSize()):
            minIndex = parentIndex
            if self.pq[minIndex].priority > self.pq[leftIndex].priority:
                minIndex = leftIndex
            if (rightIndex < self.getSize() and self.pq[minIndex].priority > self.pq[rightIndex].priority):
                minIndex = rightIndex

            if minIndex != parentIndex:
                self.pq[parentIndex], self.pq[minIndex] = self.pq[minIndex], self.pq[parentIndex]
                parentIndex = minIndex
                leftIndex = 2 * parentIndex + 1
                rightIndex = 2 * parentIndex + 2
            else:
                break

    def removeMin(self):
        if self.isEmpty():
            return None
        element = self.pq[0]

        self.pq[0] = self.pq[self.getSize() - 1]
        self.pq.pop()
        self.downheapify()
        return element.ele


myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i = 1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i += 1
        myPq.insert(element, element)
    elif choice == 2:
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i += 1
