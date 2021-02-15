from typing import List


class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]
        longest = 1
        for i in range(n):
            j = 0
            while j < i:
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
                j += 1

            longest = max(dp[i], longest)

        return longest

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[0]]
        i = 1
        while i < n:
            dn = len(dp) - 1
            if nums[i] > dp[dn]:
                dp.append(nums[i])
            else:
                index = self.binSearch(dp, 0, len(dp) - 1, nums[i])
                dp[index] = nums[i]

            i += 1
        return len(dp)

    def binSearch(self, dp, start, end, k):

        while start <= end:
            mid = (start + end) // 2
            if dp[mid] == k:
                return mid
            elif k < dp[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return start


if __name__ == "__main__":
    arr = list(map(int, input().strip().split(" ")))
    s = Solution().lengthOfLIS(arr)
    print(s)
