from typing import List
from collections import  deque

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        t1 = self.maxProductHelper(nums)
        nums.reverse()
        t2 = self.maxProductHelper(nums)
        return max(t1, t2)

    def maxProductHelper(self, nums: List[int]) -> int:
        sum_before_lst_neg_index = None
        curr = 1
        lst_negative_index = None
        i = 0
        mxx = nums[0]
        n = len(nums)
        while i < n:
            v = nums[i]
            mxx = max(v, mxx)
            if v < 0:
                if lst_negative_index is None:
                    lst_negative_index = i
                    sum_before_lst_neg_index = curr
                    curr = 1
                else:
                    curr = sum_before_lst_neg_index * curr * nums[lst_negative_index] * nums[i]
                    lst_negative_index = None
                    sum_before_lst_neg_index = None
                    mxx = max(curr, mxx)
            elif v == 0:
                curr = 1
                sum_before_lst_neg_index = None
                lst_negative_index = None
            else:
                curr *= v
                if v == 1:
                    flag = True
                mxx = max(curr, mxx)
            i += 1

        mxx = int(mxx)
        return int(mxx)


if __name__ == "__main__":
    arr = list(map(int, input().strip()[1:-1].split(",")))
    s = Solution().maxProduct(arr)
    print(s)
