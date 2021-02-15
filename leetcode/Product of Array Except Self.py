from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        t = 1
        for v in nums:
            t *= v
            output.append(t)

        t = nums[n - 1]
        output[n - 1] = output[n - 2]
        for i in range(n - 2, 0, -1):
            v=nums[i]
            output[i] = output[i - 1] * t
            t *= v

        output[0] = t

        return output


if __name__ == "__main__":
    arr = list(map(int, input().strip()[1:-1].split(",")))
    s = Solution().productExceptSelf(arr)
    print(s)
