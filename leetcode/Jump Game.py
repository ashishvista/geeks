class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        j = 0
        n = len(nums)
        for i in range(n):
            if i > j:
                return False
            elif j >= n - 1:
                return True
            elif j < nums[i] + i:
                j = nums[i] + i


if __name__ == "__main__":
    arr = list(map(int, input()[1:-1].strip().split(",")))
    s = Solution()
    print(s.canJump(arr))
