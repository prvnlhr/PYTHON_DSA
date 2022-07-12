import heapq


class Median:

    def __init__(self):
        self.sortedLeftHalf = []
        self.sortedRightHalf = []

    def addNum(self, num):

        # edge case: if first element means maxHeap i.e sortedRightHalf is empty
        if len(self.sortedRightHalf) == 0:
            heapq.heappush(self.sortedRightHalf, -num)
            return

        if num <= -self.sortedRightHalf[0]:
            heapq.heappush(self.sortedRightHalf, -num)
        else:
            heapq.heappush(self.sortedLeftHalf, num)

        if len(self.sortedRightHalf) - len(self.sortedLeftHalf) == 2:
            heapq.heappush(self.sortedLeftHalf, -heapq.heappop(self.sortedRightHalf))


        elif len(self.sortedRightHalf) - len(self.sortedLeftHalf) == -2:
            heapq.heappush(self.sortedRightHalf, -heapq.heappop(self.sortedLeftHalf))

    def findMedain(self, num):
        self.addNum(num)
        print(self.sortedLeftHalf)
        print(self.sortedRightHalf)

        if len(self.sortedRightHalf) == len(self.sortedLeftHalf):
            median = (self.sortedLeftHalf[0] - self.sortedRightHalf[0]) / 2
            return median

        else:

            return self.sortedLeftHalf[0] if len(self.sortedLeftHalf) > len(self.sortedRightHalf) else \
                -self.sortedRightHalf[0]


obj = Median()

streamOfIntegers = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]

for num in streamOfIntegers:
    print('median after reading', num, 'is', obj.findMedain(num))
#
# []
# [-5]
# median after reading 5 is 5
# [15]
# [-5]
# median after reading 15 is 10.0
# [15]
# [-5, -1]
# median after reading 1 is 5
# [5, 15]
# [-3, -1]
# median after reading 3 is 4.0
# [5, 15]
# [-3, -1, -2]
# median after reading 2 is 3
# [5, 15, 8]
# [-3, -1, -2]
# median after reading 8 is 4.0
# [5, 7, 8, 15]
# [-3, -1, -2]
# median after reading 7 is 5
# [5, 7, 8, 15, 9]
# [-2, -1, 3]
# median after reading 9 is 5
# [5, 7, 8, 15, 9, 10]
# [-2, -1, 3]
# median after reading 10 is 5
# [5, 7, 6, 15, 9, 10, 8]
# [-2, -1, 3]
# median after reading 6 is 5
# [5, 7, 6, 11, 9, 10, 8, 15]
# [-2, -1, 3]
# median after reading 11 is 5
# [4, 5, 6, 7, 9, 10, 8, 15, 11]
# [-2, -1, 3]
# median after reading 4 is 4
