from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i = n - 1
        next_num_flag = False
        while i > 0:
            if nums[i - 1] >= nums[i]:
                i -= 1
                continue
            else:
                next_num_flag = True
                break

        if not next_num_flag:
            return nums.sort()

        k = i - 1

        for i in range(n - 1, k, -1):
            if nums[i] > nums[k]:
                nums[i], nums[k] = nums[k], nums[i]
                break

        i = k + 1
        j = n - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return nums


if __name__ == "__main__":
    nums = input()
    list1 = []
    list1[:0] = nums
    list1 = nums = list(map(int, list1))
    res = Solution().nextPermutation(nums)
    print(res)
