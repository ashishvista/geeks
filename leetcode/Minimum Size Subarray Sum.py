from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        start = 0
        mx = nums[0]
        sum = nums[0]
        tmp = []
        end = None
        for i in range(1, n):
            mx = max(mx, nums[i])
            sum += nums[i]

            if sum >= s:
                end = i
                break

        if mx >= s:
            return 1
        if not end:
            return 0
        mx = end - start + 1
        tmp = nums[start:end + 1]
        while start < end:

            while start < end:
                sum -= nums[start]
                start += 1
                tmp = nums[start:end + 1]
                if sum < s:
                    break
                else:
                    ln = end - start + 1
                    mx = min(mx, ln)

            while end < n - 1:
                sum -= nums[start]
                start += 1
                end += 1
                sum += nums[end]
                tmp = nums[start:end + 1]
                if sum >= s:
                    ln = end - start + 1
                    mx = min(mx, ln)
                    break

        return mx


if __name__ == "__main__":
    s = int(input())
    arr = list(map(int, input().strip()[1:-1].split(",")))
    Solution().minSubArrayLen(s, arr)
