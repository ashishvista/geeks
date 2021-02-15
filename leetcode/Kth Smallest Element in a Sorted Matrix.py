class Node:

    def __init__(self, i, j, v):
        self.i = i
        self.j = j
        self.v = v


class Solution:
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][k - 1]
        arr = self.kthSmallestHelper(matrix, 0, n - 1)
        print(arr)
        return arr[k - 1]

    def kthSmallestHelper1(self, matrix, start, end):
        n = len(matrix)
        if start == end:
            return matrix[start]
        mid = (start + end) // 2

        left = self.kthSmallestHelper(matrix, start, mid)
        right = self.kthSmallestHelper(matrix, mid + 1, end)

        ln = len(left)
        rn = len(right)

        narr = []
        i = j = 0

        while i < ln and j < rn:
            if left[i] <= right[j]:
                narr.append(left[i])
                i += 1
            else:
                narr.append(right[j])
                j += 1

        while i < ln:
            narr.append(left[i])
            i += 1

        while j < rn:
            narr.append(right[j])
            j += 1

        return narr

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        m = len(matrix[0])
        n = len(matrix)
        arr = [Node(0, j, matrix[0][j]) for j in range(m)]

        self.buildHeap(arr)
        while k > 0:
            res = arr[0]
            if res.i < n - 1:
                arr[0] = Node(res.i + 1, res.j, matrix[res.i + 1][res.j])
            else:
                tmp_node = arr.pop()
                if arr:
                    arr[0] = tmp_node
            self.heapify(arr, 0)
            k -= 1

        return res.v

    def buildHeap(self, arr):
        n = len(arr)
        k = (n - 2) // 2
        while k >= 0:
            self.heapify(arr, k)
            k -= 1

    def heapify(self, arr, p):
        n = len(arr)
        lc = p * 2 + 1
        rc = p * 2 + 2

        smallesti = p

        if lc < n and self.comparator(arr[lc], arr[smallesti]):
            smallesti = lc

        if rc < n and self.comparator(arr[rc], arr[smallesti]):
            smallesti = rc

        if smallesti != p:
            arr[smallesti], arr[p] = arr[p], arr[smallesti]
            self.heapify(arr, smallesti)


    def comparator(self, node1, node2):
        if node1.v < node2.v:
            return True
        return False
