from typing import List


class Solution:
    def canPartitionKSubsets1(self, nums: List[int], k: int) -> bool:
        sum = 0
        if len(nums) < k:
            return False

        for i in nums:
            sum += i

        if sum % k > 0:
            return False

        nums.sort()

        target = sum // k

        if nums[-1] > target:
            return False

        groups = [0 for i in range(k)]
        return self.canPartitionKSubsetsHelper(nums, target, groups)

    def canPartitionKSubsetsHelper(self, nums, target, groups):

        if len(nums) == 0:
            return True

        item = nums.pop()

        for i, group in enumerate(groups):

            if group + item <= target:
                groups[i] += item
                if self.canPartitionKSubsetsHelper(nums, target, groups):
                    return True
                groups[i] -= item

            if group == 0:
                break

        nums.append(item)

        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        if k > n:
            return False

        sum = 0
        for i in nums:
            sum += i

        if sum % k > 0:
            return False

        target = sum // k

        for i in nums:
            if i > target:
                return False

        dp = [-1 for i in range(1 << n)]

        dp[0] = 0

        for i in range(1 << n):
            if dp[i] == -1:
                continue

            for j, num in enumerate(nums):

                if (i & 1 << j) == 0 and dp[i] + num <= target:
                    dp[i | 1 << j] = (dp[i] + num) % target

        if dp[(1 << n) - 1] == 0:
            return True
        else:
            return False
