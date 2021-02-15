from typing import List


class Solution:
    def subarraySum1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        t = 0
        c = 0
        for i in range(n):
            t = t + nums[i]
            tmp = t
            if tmp == k:
                c += 1
            for j in range(i):
                tmp -= nums[j]
                if tmp == k:
                    c += 1
        return c

    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        c = 0
        cs = []
        s = 0
        hash = {}

        for i in range(n):
            s += nums[i]
            if s == k:
                c += 1

            if s in hash:
                c = c + hash[s]

            v = s + k
            if v in hash:
                hash[v] += 1
            else:
                hash[v] = 1

        return c


if __name__ == "__main__":
    arr = list(map(int, input().strip()[1:-1].split(",")))
    k = int(input())
    s = Solution().subarraySum(arr, k)
    print(s)
