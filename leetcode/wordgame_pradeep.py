class Solution:
    no_of_solutions = 0
    total_matrix_generated = 0

    def wordGame(self, strs):
        n = 3
        matrix = [[0 for i in range(n)] for i in range(n)]
        h = {}
        for s in strs:
            for v in s:
                if v not in h:
                    h[v] = 1
        pos = []
        for i in range(n):
            for j in range(n):
                pos.append([i, j])

        self.generateMatrixHelper(strs, h, n, 0, pos, matrix)
        print(self.no_of_solutions)

    def generateMatrixHelper(self, strs, h, n, pos_i, pos, matrix):

        if pos_i == (n * n):
            self.total_matrix_generated += 1

            # matrix = [['z', 'e', 'd'],
            #           ['o', 'l', 'd'],
            #           ['o', 'a', 't']]

            if self.searchAllWordsExists(strs, matrix, n):
                self.no_of_solutions += 1
                print(matrix, self.total_matrix_generated, self.no_of_solutions)

            return

        i = pos[pos_i][0]
        j = pos[pos_i][1]

        for v in h:
            matrix[i][j] = v
            self.generateMatrixHelper(strs, h, n, pos_i + 1, pos, matrix)

    def searchAllWordsExists(self, strs, matrix, n):

        for ss in strs:
            flag = False
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] == ss[0]:
                        if self.searchWordExistsHelper(ss, i, j, matrix, n):
                            flag = True
                            break
                if flag:
                    break

            if not flag:
                return False

        return True

    def searchWordExistsHelper(self, ss, i, j, matrix, n):

        dirs = [[1, 0], [0, 1], [1, 1], [1, -1], [-1, 0], [0, -1], [-1, -1], [-1, 1]]

        for d in dirs:
            p = d[0]
            q = d[1]

            k = 0
            flag = True
            ni = i
            nj = j
            for index, v in enumerate(ss):

                if ni >= 0 and ni < n and nj >= 0 and nj < n and matrix[ni][nj] == ss[k]:
                    k += 1
                    ni += p
                    nj += q
                    continue
                else:
                    flag = False
                    break

            if flag:
                return True

        return False


if __name__ == "__main__":
    s = list(input().strip().split(" "))
    res = Solution().wordGame(s)
    print(res)
