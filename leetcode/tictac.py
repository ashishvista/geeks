class Solution:
    def tictac(self):
        self.n = 3
        self.mat = [[-1 for i in range(3)] for i in range(3)]

    def isGameDraw(self):
        status = self.isPlayerWinner(self, 1, )
        self.isPlayerWinner(self, 0, )

    def isPlayerWinner(self, player):
        mat = self.mat
        n = self.n
        ###row wise checking
        for i in range(n):
            flag = True
            for j in range(n):
                if mat[i][j] != player or mat[i][j] != -1:
                    flag = False
                    break
            if flag:
                return True

        # column wise checking
        for i in range(n):
            flag = True
            for j in range(n):
                if mat[j][i] != player or mat[j][i] != -1:
                    flag = False
                    break
            if flag:
                return True

        # diagonal wise checking from left to right
        flag = True
        for i in range(n):
            if mat[i][i] != player or mat[i][i] != -1:
                flag = False
                break

        if flag:
            return True

        # diagonal wise checking from right  to left
        i = 0
        j = n - 1

        flag = True
        while i < n:
            if mat[i][j] != player or mat[i][j] != -1:
                flag = False
                break
            i += 1
            j -= 1

        if flag:
            return True

        return False
