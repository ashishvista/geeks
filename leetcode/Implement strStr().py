class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        hn = len(haystack)
        nn = len(needle)
        if needle == "":
            return 0
        lps = self.getLps(needle)
        while i < hn:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == nn:
                    return i - nn
            elif j == 0:
                i += 1
            else:
                j = lps[j - 1]

        return -1

    def getLps(self, s: str) -> str:
        n = len(s)
        lps = [0 for i in range(n)]
        i = 1
        ln = 0
        lps[0] = 0
        while i < n:
            if s[ln] == s[i]:
                ln += 1
                lps[i] = ln
                i += 1
            elif ln == 0:
                i += 1
            else:
                ln = lps[ln - 1]
        return lps


if __name__ == "__main__":
    haystack = input()[1:-1]
    needle = input()[1:-1]
    res = Solution().strStr(haystack, needle)
    print(res)
