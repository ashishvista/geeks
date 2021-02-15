from typing import List


class Solution:
    hash = {}
    uniq = []
    res = []

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        self.hash = {}
        self.hash[float("-inf")] = -1
        self.uniq = []
        self.res = []

        n = len(nums)
        for i in range(n):
            if nums[i] in self.hash:
                self.hash[nums[i]] += 1
            else:
                self.hash[nums[i]] = 1
                self.uniq.append(nums[i])

        un = len(self.uniq)
        self.topKFrequentHelper(self.uniq, un, k)
        # self.topKFrequentHelper(nums, n, n)

        return self.res

    def heapify(self, p, nums, n):
        lv = float("-inf")
        rv = float("-inf")

        lc = 2 * p + 1
        rc = 2 * p + 2

        if lc < n:
            lv = nums[lc]

        if rc < n:
            rv = nums[rc]

        largest = p

        # if nums[p] < lv:
        #     largest = lc
        #
        # if nums[largest] < rv:
        #     largest = rc
        if self.compare(nums[p], lv):
            largest = lc

        if self.compare(nums[largest], rv):
            largest = rc

        if largest == lc:
            nums[p], nums[lc] = nums[lc], nums[p]
            self.heapify(lc, nums, n)
        elif largest == rc:
            nums[p], nums[rc] = nums[rc], nums[p]
            self.heapify(rc, nums, n)

    def compare(self, a, b):
        if self.hash[a] < self.hash[b]:
            return True
        else:
            return False

    def createMaxheap(self, nums, n):
        j = (n - 2) // 2
        for i in range(j, -1, -1):
            self.heapify(i, nums, n)

    def topKFrequentHelper(self, nums, n, k):
        self.createMaxheap(nums, n)

        k -= 1
        self.res.append(nums[0])
        nums[0], nums[n - 1] = nums[n - 1], nums[0]

        tmp_n = n - 1

        while k > 0:
            self.heapify(0, nums, tmp_n)
            self.res.append(nums[0])
            nums[0], nums[tmp_n - 1] = nums[tmp_n - 1], nums[0]
            tmp_n -= 1
            k -= 1


if __name__ == "__main__":
    arr = list(map(int, input().strip()[1:-1].split(",")))
    k = int(input())
    s = Solution().topKFrequent(arr, k)
    print(s)
