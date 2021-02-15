from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        visited = [[False for i in range(n)] for i in range(m)]
        dir = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        for i in range(m):
            for j in range(n):
                item = board[i][j]
                if item == "O" and not visited[i][j]:
                    self.bfs(board, m, n, visited, i, j, dir)

    def bfs(self, board, m, n, visited, i, j, dir):
        dq = deque()
        dq.append([i, j])
        visited[i][j] = True
        isSurrounded = True
        st = [[i, j]]

        while dq:
            item = dq.popleft()
            i = item[0]
            j = item[1]
            for d in dir:
                x = i + d[0]
                y = j + d[1]
                if not self.isValid(m, n, x, y):
                    isSurrounded = False

                elif board[x][y] == "O" and not visited[x][y]:
                    dq.append([x, y])
                    visited[x][y] = True
                    st.append([x, y])

        if isSurrounded:
            for item in st:
                x = item[0]
                y = item[1]
                board[x][y] = "X"

    def isValid(self, m, n, i, j):
        if i >= 0 and i < m and j >= 0 and j < n:
            return True
        return False
