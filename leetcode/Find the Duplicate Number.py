from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t = nums[0]
        h = nums[0]

        while True:
            t = nums[t]
            h = nums[nums[h]]
            if h == t:
                break

        t = nums[0]
        while h != t:
            t = nums[t]
            h = nums[h]

        return h


if __name__ == "__main__":
    arr = list(map(int, input()[1:-1].strip().split(",")))
    s = Solution().findDuplicate(arr)
    print(s)
