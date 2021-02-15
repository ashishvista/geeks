from collections import deque


class Node:

    def __init__(self, i, j, path):
        self.i = i
        self.j = j
        self.path = path


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        m = len(matrix[0])
        n = len(matrix)

        self.dp = [[None for i in range(m)] for i in range(n)]
        self.mxx = 0

        for i in range(n):
            for j in range(m):
                self.mxx = max(self.dfs(i, j, m, n, matrix), self.mxx)

        return self.mxx

    def dfs(self, i, j, m, n, matrix):
        if self.dp[i][j]:
            return self.dp[i][j]

        mxx = 0

        for dir in self.dirs:
            x = i + dir[0]
            y = j + dir[1]
            if self.isValid(m, n, x, y) and matrix[x][y] > matrix[i][j]:
                mxx = max(self.dfs(x, y, m, n, matrix), mxx)

        self.dp[i][j] = mxx + 1
        return self.dp[i][j]



    def isValid(self, m, n, i, j):
        if i >= 0 and i < n and j >= 0 and j < m:
            return True
        return False
