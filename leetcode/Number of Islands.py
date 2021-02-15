from collections import deque


class Solution:
    def isValid(self, i, j, m, n):
        if i >= 0 and i < m and j >= 0 and j < n:
            return True
        return False

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False for i in range(n)] for i in range(m)]
        count = 0
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    count += 1
                    q = deque()
                    visited[i][j] = True
                    q.append([i, j])

                    while q:
                        item = q.popleft()
                        x = item[0]
                        y = item[1]
                        for d in directions:
                            a = x + d[0]
                            b = y + d[1]

                            if self.isValid(a, b, m, n) and grid[a][b] == "1" and not visited[a][b]:
                                visited[a][b] = True
                                q.append([a, b])
        return count
