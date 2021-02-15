class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])

        dir = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

        for i in range(m):
            for j in range(n):
                lnc = 0
                for cord in dir:
                    x = i + cord[0]
                    y = j + cord[1]
                    if self.isValid(m, n, x, y):
                        p = board[x][y]
                        if p == -1:
                            p = 1
                        elif p == 2:
                            p = 0
                        if p == 1:
                            lnc += 1

                if board[i][j] == 1:
                    if lnc < 2 or lnc > 3:
                        board[i][j] = -1
                else:
                    if lnc == 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0

    def isValid(self, m, n, i, j):
        if i >= 0 and j >= 0 and i < m and j < n:
            return True
        return False
