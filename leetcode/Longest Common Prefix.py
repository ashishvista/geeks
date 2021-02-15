from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        if not strs:
            return ""
        p = strs[0]
        n = len(strs)
        i = 0
        lcp = ""
        while i < len(p):
            for j in range(1, n):
                s = strs[j]
                if i < len(s) and p[i] != s[i]:
                    return lcp
                elif i == len(s):
                    return lcp
            lcp += p[i]
            i += 1

        return lcp


if __name__ == "__main__":
    arr = list(input().split())
    s = Solution().longestCommonPrefix(arr)
    print(s)
