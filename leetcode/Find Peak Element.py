from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        n = len(nums)
        end = n - 1

        while start <= end:
            mid = (start + end) // 2
            cur = nums[mid]
            prev = float("-inf")
            next = float("-inf")
            if mid > 0:
                prev = nums[mid - 1]
            if mid < n - 1:
                next = nums[mid + 1]

            if prev < cur and next < cur:
                return mid
            elif next > cur:
                start = mid + 1
            else:
                end = mid - 1


if __name__ == "__main__":
    arr = list(map(int, input().strip()[1:-1].split(",")))
    res = Solution().findPeakElement(arr)
    print(res)
