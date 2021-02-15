from typing import List


class Solution:
    def findTargetSumWays1(self, nums: List[int], S: int) -> int:
        t = 0
        for v in nums:
            t += v

        n = len(nums)
        dp = {}

        x = self.findTargetSumWaysHelper(nums, 0, nums[0], dp, S)
        y = self.findTargetSumWaysHelper(nums, 0, -1 * nums[0], dp, S)

        return x + y

    def findTargetSumWaysHelper(self, nums, i, t, dp, S):
        if i == len(nums) - 1:
            if t == S:
                return 1
            else:
                return 0

        index = str(i) + "#" + str(t)
        if index in dp:
            return dp[index]
        x = self.findTargetSumWaysHelper(nums, i + 1, t + nums[i + 1], dp, S)

        y = self.findTargetSumWaysHelper(nums, i + 1, t + nums[i + 1] * -1, dp, S)

        dp[index] = x + y
        return x + y

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        h = {}
        if nums[0] == 0:
            h[nums[0]] = 2
        else:
            h[nums[0]] = 1
            h[nums[0] * -1] = 1

        n = len(nums)
        for i in range(1, n):
            tmp = {}
            p = nums[i] * -1
            q = nums[i]
            for v in h:
                r = v + p
                s = v + q
                if r in tmp:
                    tmp[r] += h[v]
                else:
                    tmp[r] = h[v]
                if s in tmp:
                    tmp[s] += h[v]
                else:
                    tmp[s] = h[v]
            h = tmp

        if S in h:
            return h[S]
        else:
            return 0


if __name__ == "__main__":
    arr = list(map(int, input().strip()[1:-1].split(",")))
    target = int(input())
    s = Solution().findTargetSumWays(arr, target)
    print(s)
