class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        print()
        wordHash = {}
        for v in wordDict:
            wordHash[v] = 1

        del wordDict

        dp = [True for i in range(len(s))]
        n = len(s)

        return self.wordBreakHelper(s, 0, wordHash, dp, n)

    def wordBreakHelper(self, s, i, wordHash, dp, n):
        if i == n:
            return True

        if not dp[i]:
            return False

        for j in range(i, n):
            k = j + 1
            if s[i:k] in wordHash:
                r = self.wordBreakHelper(s, k, wordHash, dp, n)
                if r:
                    return True
                else:
                    dp[k] = False

        return False
