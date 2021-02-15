from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = 0
        n = len(nums)
        for v in nums:
            s += v
        p = s / 2
        q = s // 2

        if p - q > 0:
            return False
        dp = [False for i in range(q + 1)]
        dp[0] = True

        ts = nums[0]
        if ts <= q:
            dp[ts] = True
        for i in range(1, n):
            v = nums[i]
            for j in range(min(ts, q), -1, -1):
                z = j + v
                if z > q:
                    continue
                if dp[j]:
                    dp[z] = True
                if dp[q]:
                    return True
            ts += v

        return False


if __name__ == "__main__":
    arr = list(map(int, input().strip()[1:-1].split(",")))
    s = Solution().canPartition(arr)
    print(s)
