from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = c = len(matrix)
        m = 0
        n = r - 1

        while m < n:
            i = m
            for j in range(m, n):
                # print(i, j)
                # print(j, n)
                # print(n, c - j - 1)
                # print(c - j - 1, m)
                temp1 = matrix[j][n]
                matrix[j][n] = matrix[i][j]

                temp2 = matrix[n][c - j - 1]
                matrix[n][c - j - 1] = temp1

                temp3 = matrix[c - j - 1][m]
                matrix[c - j - 1][m] = temp2

                matrix[i][j] = temp3
                # print(matrix)
            m += 1
            n -= 1


if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    for i in range(n):
        tmp = list(map(int, input().strip().split()))
        arr.append(tmp)
    s = Solution()
    s.rotate(arr)
    print(arr)
