class Solution:
    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        h = {}
        n = 9
        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num != "." and num in h:
                    print("111", i, j)
                    return False
                else:
                    h[num] = 1
            h = {}

        for i in range(n):
            for j in range(n):
                num = board[j][i]
                if num != "." and num in h:
                    print("2222", j, i)

                    return False
                else:
                    h[num] = 1
            h = {}

        arr = [0, 3, 6]
        for i in arr:
            for j in arr:
                h = {}
                print("boardddd", i, j)
                for x in range(3):
                    for y in range(3):
                        num = board[i + x][j + y]
                        if num != "." and num in h:
                            print("3333", i + x, j + y)
                            return False
                        else:
                            h[num] = 1
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):

                bnr = i // 3
                bnc = j // 3
                bn = bnr * 3 + bnc
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[bn]:
                    return False
                else:
                    rows[i][board[i][j]] = cols[j][board[i][j]] = boxes[bn][board[i][j]] = 1

        return True
