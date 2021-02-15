class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for i in range(n)]
        count = 0

        for size in range(1, n + 1):
            for start in range(n - size + 1):
                end = start + size - 1

                if start == end:
                    dp[start][end] = 1
                    count += 1
                elif s[start] == s[end] and (dp[start + 1][end - 1] or start + 1 > end - 1):
                    dp[start][end] = 1
                    count += 1

        return count


if __name__ == "__main__":
    ss = input()[1:-1]
    s = Solution().countSubstrings(ss)
    print(s)
