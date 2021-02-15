class Solution:
    def shortestPalindrome(self, s: str) -> str:
        sr = s + "#" + s[::-1]
        k = self.longestPrefix(sr)

        rs = s[k:]
        return rs[::-1] + s

    def longestPrefix(self, s: str) -> str:
        n = len(s)
        kmp = [0 for i in range(n)]
        i = 1
        ln = 0
        kmp[0] = 0
        while i < n:
            if s[ln] == s[i]:
                ln += 1
                kmp[i] = ln
                i += 1
            elif ln == 0:
                i += 1
            else:
                ln = kmp[ln - 1]
        k = kmp[n - 1]
        return k


if __name__ == "__main__":
    ss = input()
    res = Solution().shortestPalindrome(ss)
    print(res)
