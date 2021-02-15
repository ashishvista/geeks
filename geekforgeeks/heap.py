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

    def getTopValue(self):
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

    def remove(self, i):
        v = self.getTopValue()
        self.arr[i] = v
        while True:
            p = self.parent(i)
            if p >= 0 and self.compare(p, i):
                self.arr[p], self.arr[i] = self.arr[i], self.arr[p]
                i = p
            else:
                break
        self.extractTop()


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

    def getTopValue(self):
        return float("-inf")


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

    def getTopValue(self):
        return float("inf")


# if __name__ == "__main__":
#     arr = [5, 10, 1, 2, 0, 3, 9, 1]
#     h = MaxHeap()
#     for i in arr:
#         h.insert(i)
#         print(h.getTop())
#     print("######################")
#     h.remove(5)
#     print(h.getTop())
