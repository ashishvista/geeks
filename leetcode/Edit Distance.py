class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        self.dp = [[-1 for i in range(l2 + 1)] for i in range(l1 + 1)]
        return self.minDistanceHelper(word1, word2, l1 - 1, l2 - 1)

    def minDistanceHelper(self, word1, word2, i, j):
        if i == -1 and j == -1:
            return 0
        elif i == -1 and j >= 0:
            return j + 1
        elif j == -1 and i >= 0:
            return i + 1

        if self.dp[i][j] > -1:
            return self.dp[i][j]
        if word1[i] == word2[j]:
            res = self.minDistanceHelper(word1, word2, i - 1, j - 1)
        else:
            p = 1 + self.minDistanceHelper(word1, word2, i, j - 1)  # insert
            q = 1 + self.minDistanceHelper(word1, word2, i - 1, j - 1)  # replace
            r = 1 + self.minDistanceHelper(word1, word2, i - 1, j)  # delete
            res = min(p, q, r)

        self.dp[i][j] = res
        return res


if __name__ == "__main__":
    w1 = input()[1:-1]
    w2 = input()[1:-1]
    s = Solution().minDistance(w1, w2)
    print(s)
