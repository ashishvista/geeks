from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, v in enumerate(nums):
            if target - v in hash:
                return [i, hash[target - v]]
            else:
                hash[v] = i


if __name__ == "__main__":
    nums = list(map(int, input()[1:-1].strip().split(',')))
    target = int(input())
    sum = Solution()
    print(sum.twoSum(nums, target))
