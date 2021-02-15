from typing import List


class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = -1
        for i, v in enumerate(nums):
            if v == 0:
                break

        if i == -1:
            return
        while True:
            j = i + 1

            while j < n:
                if nums[j] != 0:
                    break
                j += 1
            if j == n:
                return
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    def moveZeroes(self, nums: List[int]) -> None:
        count = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1


if __name__ == "__main__":
    nums = list(map(int, input()[1:-1].strip().split(",")))
    s = Solution()
    s.moveZeroes(nums)
    print(nums)
