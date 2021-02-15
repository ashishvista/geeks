from typing import List


class Solution:
    res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        tmp = []
        self.res = []
        self.permuteHelper(nums, 0, n, tmp)
        return self.res

    def permuteHelper(self, nums, start, n, tmp):
        if start >= n:
            self.res.append(tmp.copy())
            return
        for i in range(start, n):
            nums[start], nums[i] = nums[i], nums[start]
            tmp.append(nums[start])
            self.permuteHelper(nums, start + 1, n, tmp)
            tmp.pop()
            nums[start], nums[i] = nums[i], nums[start]


if __name__ == "__main__":
    arr = list(map(int, input()[1:-1].strip().split(",")))
    res = Solution().permute(arr)
    print(res)
