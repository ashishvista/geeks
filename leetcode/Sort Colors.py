class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        j = 0
        k = n - 1

        while j <= k:
            if nums[j] == 1:
                j += 1
                continue
            elif nums[j] == 0:
                nums[j] = 1
                nums[i] = 0
                j += 1
                i += 1
            else:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1


