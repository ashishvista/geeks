from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        ex = 0
        inc = nums[0]
        for i in range(1, n):
            ex_temp = max(inc,ex)
            inc_temp = ex + nums[i]
            ex = ex_temp
            inc = inc_temp

        return max(inc, ex)


if __name__ == "__main__":
    arr = list(map(int, input()[1:-1].strip().split(",")))
    s = Solution()
    print(s.rob(arr))
