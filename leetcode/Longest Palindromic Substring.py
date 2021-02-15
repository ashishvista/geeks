class Solution:
    def longestPalindrome1(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return None
        dp = [[False for i in range(n)] for i in range(n)]
        size = 3
        longest = 1
        longest_str = []

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                longest = 2
                longest_str = [i, i + 1]
        while size <= n:

            for i in range(n - size + 1):
                start = i
                end = start + size - 1
                if dp[start + 1][end - 1]:
                    if s[start] == s[end]:
                        dp[start][end] = True
                        pal_len = end - start + 1
                        if longest < pal_len:
                            longest = pal_len
                            longest_str = [start, end]
                    else:
                        dp[start][end] = False
            size += 1
        if longest == 1:
            return s[0]
        else:
            return s[longest_str[0]:longest_str[1] + 1]

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return None
        longest = 1
        longest_str = []
        for k in range(n):
            i = k
            j = k + 1
            while i >= 0 and j < n and s[i] == s[j]:
                size = j - i + 1
                if size > longest:
                    longest = size
                    longest_str = [i, j]
                i -= 1
                j += 1

            i = k - 1
            j = k + 1

            while i >= 0 and j < n and s[i] == s[j]:
                size = j - i + 1
                if size > longest:
                    longest = size
                    longest_str = [i, j]
                i -= 1
                j += 1

        if longest == 1:
            return s[0]
        else:
            return s[longest_str[0]:longest_str[1] + 1]


if __name__ == "__main__":
    s = input().strip()[1:-1]
    s = Solution().longestPalindrome(s)
    print(s)
