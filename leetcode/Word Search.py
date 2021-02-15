class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False for i in range(n)] for i in range(m)]
        dir = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    res = self.existsHelper(board, i, j, m, n, word, dir, visited, 0)
                    if res:
                        return True

    def existsHelper(self, board, i, j, m, n, word, dir, visited, k):
        if k == len(word) - 1:
            return True
        visited[i][j] = True

        for d in dir:
            x = i + d[0]
            y = j + d[1]
            if self.isValid(x, y, m, n) and not visited[x][y] and board[x][y] == word[k + 1]:
                res = self.existsHelper(board, x, y, m, n, word, dir, visited, k + 1)
                if res:
                    return True
                
        visited[i][j] = False

        return False

    def isValid(self, i, j, m, n):
        if i >= 0 and i < m and j >= 0 and j < n:
            return True
        return False
