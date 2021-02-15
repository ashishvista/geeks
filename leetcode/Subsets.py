class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        i = 0
        n = len(nums)
        res = []
        self.subsetsHelper(nums, 0, n, res, [])
        return res

    def subsetsHelper(self, nums, i, n, res, tmp):
        if i == n:
            res.append(list.copy(tmp))
            return
        tmp.append(nums[i])
        self.subsetsHelper( nums, i + 1, n, res, tmp)
        tmp.pop()
        self.subsetsHelper( nums, i + 1, n, res, tmp)
