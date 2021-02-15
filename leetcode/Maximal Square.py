from typing import List


class Solution:
    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])

        dp = [[0 for i in range(n)] for i in range(m)]
        mxx = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    if i - 1 >= 0 and j - 1 >= 0:
                        mn = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                        if mn > 0:
                            dp[i][j] = mn + 1
                    mxx = max(mxx, dp[i][j])
        return (mxx * mxx)

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])

        dp = [0 for i in range(n)]
        mxx = 0
        for i in range(m):
            for j in range(n):
                k = int(matrix[i][j])
                if matrix[i][j] == "1" and i - 1 >= 0 and j - 1 >= 0:
                    mn = min(dp[j - 1], prev, dp[j])
                    if mn > 0:
                        k = mn + 1
                prev = dp[j]
                dp[j] = k
                mxx = max(mxx, dp[j])

        return mxx * mxx


if __name__ == "__main__":
    arr = []
    m = int(input())
    for i in range(m):
        arr.append(list(input().strip().split(" ")))
    s = Solution().maximalSquare(arr)
    print(s)
