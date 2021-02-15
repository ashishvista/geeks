class Solution:
    def climbStairs(self, n: int) -> int:
        pp = 1
        p = 2

        if n == 1:
            return 1
        elif n == 2:
            return 2

        for i in range(3, n + 1):
            curr = p + pp
            pp = p
            p = curr

        return curr


if __name__ == "__main__":
    n = int(input())
    s = Solution().climbStairs(n)
    print(s)
