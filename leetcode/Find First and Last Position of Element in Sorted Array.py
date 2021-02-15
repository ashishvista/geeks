from typing import List


class Solution:
    def searchRangeHelper(self, nums, target, start, end):
        flag = False
        hash = {}
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                flag = True
                break
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        if flag:
            hash["start"] = start
            hash["end"] = end
            hash["mid"] = mid

            return hash
        else:
            return None

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start = 0
        end = n - 1
        ans = [-1, -1]
        res = self.searchRangeHelper(nums, target, start, end)

        if res is None:
            return ans
        else:
            leftRes = res
            rightRes = res
            while leftRes is not None:
                ans[0] = leftRes["mid"]
                leftRes = self.searchRangeHelper(nums, target, res["start"], leftRes["mid"] - 1)
            while rightRes is not None:
                ans[1] = rightRes["mid"]
                rightRes = self.searchRangeHelper(nums, target, rightRes["mid"] + 1, rightRes["end"])
        return ans


if __name__ == "__main__":
    nums = list(map(int, input().strip()[1:-1].split(",")))
    target = int(input())
    s = Solution().searchRange(nums, target)
    print(s)
