class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        dp = [[0 for i in range(c)] for i in range(r)]

        dp[0][0] = grid[0][0]
        for i in range(1, c):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for j in range(1, r):
            dp[j][0] = dp[j - 1][0] + grid[j][0]

        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        print(dp)
        return dp[r - 1][c - 1]
