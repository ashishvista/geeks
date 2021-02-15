import sys

sys.setrecursionlimit(5000)


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        self.m = len(grid[0])
        self.n = len(grid)
        self.visited = [[False for i in range(self.m)] for i in range(self.n)]

        self.maxArea = 0
        self.area = 0
        for i in range(self.n):
            for j in range(self.m):

                if not self.visited[i][j] and grid[i][j] == 1:
                    self.dfs(i, j)
                    self.maxArea = max(self.maxArea, self.area)
                    self.area = 0

        return self.maxArea

    def dfs(self, i, j):
        self.visited[i][j] = True
        self.area += 1

        for dir in self.dirs:
            x = i + dir[0]
            y = j + dir[1]
            if self.isValid(x, y) and not self.visited[x][y] and self.grid[x][y] == 1:
                self.dfs(x, y)

    def isValid(self, i, j):
        if i >= 0 and i < self.n and j >= 0 and j < self.m:
            return True
        return False
