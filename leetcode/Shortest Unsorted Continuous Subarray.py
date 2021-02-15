from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        prev = float("-inf")
        i = 0
        while i < n and nums[i] >= prev:
            prev = nums[i]
            i += 1

        if i == n:
            return 0
        j = n - 1

        prev = float("+inf")

        while nums[j] <= prev:
            prev = nums[j]
            j -= 1

        sm = nums[i]
        lr = nums[j]

        for k in range(i + 1, n):
            if nums[k] < sm:
                sm = nums[k]

        for k in range(j - 1, -1, -1):
            if nums[k] > lr:
                lr = nums[k]

        i = 0
        while nums[i] <= sm:
            i += 1

        j = n - 1

        while nums[j] >= lr:
            j -= 1

        return j - i + 1


if __name__ == "__main__":
    arr = list(map(int, input().strip()[1:-1].split(",")))
    s = Solution().findUnsortedSubarray(arr)
    print(s)
