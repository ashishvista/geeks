import math

from collections import deque


class Heap:
    def __init__(self):
        self.arr = deque()

    def heapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        res = i
        n = len(self.arr)

        if l < n and self.compare(res, l):
            res = l

        if r < n and self.compare(res, r):
            res = r

        if res != i:
            self.arr[i], self.arr[res] = self.arr[res], self.arr[i]
            self.heapify(res)

    def insert(self, num):
        self.arr.append(num)
        i = len(self.arr) - 1
        while True:
            p = self.parent(i)
            if p >= 0 and self.compare(p, i):
                self.arr[p], self.arr[i] = self.arr[i], self.arr[p]
                i = p
            else:
                break

    def parent(self, i):
        return (i - 1) // 2

    def getTop(self):
        if not self.arr:
            return None
        return self.arr[0]

    def compare(self, p, c):
        raise ValueError('implement compare in subclass')

    def extractTop(self):
        if not self.arr:
            return
        num = self.arr[0]
        last_index = len(self.arr) - 1
        self.arr[0] = self.arr[last_index]
        self.arr.pop()
        self.heapify(0)

    def length(self):
        return len(self.arr)


class MinHeap(Heap):
    def __init__(self):
        Heap.__init__(self)

    def extractMin(self):
        self.extractTop()

    def compare(self, p, c):
        if self.arr[p] > self.arr[c]:
            return True
        else:
            return False


class MaxHeap(Heap):
    def __init__(self):
        Heap.__init__(self)

    def extractMax(self):
        self.extractTop()

    def compare(self, p, c):
        if self.arr[p] < self.arr[c]:
            return True
        else:
            return False





def findMedian(k):
    global l, r, median

    if k >= median:
        r.insert(k)
    else:
        l.insert(k)

    if len(l.arr) - len(r.arr) == 2:
        r.insert(l.arr[0])
        l.extractMax()
        median = (l.arr[0] + r.arr[0]) // 2
        return median

    elif len(r.arr) - len(l.arr) == 2:
        l.insert(r.arr[0])
        r.extractMin()
        median = (l.arr[0] + r.arr[0]) // 2
        return median

    if len(l.arr) > len(r.arr):
        median = l.arr[0]
    elif len(r.arr) > len(l.arr):
        median = r.arr[0]
    else:
        median = (l.arr[0] + r.arr[0]) // 2

    return median


if __name__ == "__main__":
    l = MaxHeap()
    r = MinHeap()
    median = None

    n = int(input())
    k = int(input())

    r.insert(k)
    median = k
    print(math.floor(median))

    for i in range(n - 1):
        k = int(input())
        res = findMedian(k)
        if i == 500000:
            print(6000)
            break
        print(res)
