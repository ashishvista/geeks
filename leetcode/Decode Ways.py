class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s) - 1

        self.dp = [None for i in range(n + 1)]
        return self.numDecodingsHelper(s, 0, n)

    def numDecodingsHelper(self, s, i, n):
        if i > n:
            return 1

        if self.dp[i] is not None:
            return self.dp[i]
        p1 = 0
        p2 = 0
        n1 = None
        n2 = None
        if i <= n:
            n1 = int(s[i])
            if n1 == 0:
                return 0
            if i + 1 <= n:
                n2 = int(s[i:i + 2])

        if n1 is not None:
            p1 = self.numDecodingsHelper(s, i + 1, n)

        if n2 is not None and n2 > 0 and n2 <= 26:
            p2 = self.numDecodingsHelper(s, i + 2, n)

        self.dp[i] = p1 + p2
        return self.dp[i]


if __name__ == "__main__":
    s = input()
    res = Solution().numDecodings(s)
    print(res)
