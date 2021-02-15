from functools import cmp_to_key
from typing import List


class Solution:
    def __init__(self):
        self.largest = ""

    def largestNumber(self, nums: List[int]) -> str:
        nums = map(lambda x: str(x), nums)
        nums = sorted(nums, key=cmp_to_key(self.comparator))
        if nums[0] == "0":
            return "0"
        return "".join(nums)

    def comparator(self, a, b):
        c = a + b
        d = b + a
        cn = int(c)
        dn = int(d)
        if cn > dn:
            return -1
        elif cn < dn:
            return 1
        else:
            return 0


if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    res = Solution().largestNumber(arr)
    print(res)
