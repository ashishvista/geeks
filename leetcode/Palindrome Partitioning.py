from typing import List


class Solution:
    def partition2(self, s: str) -> List[List[str]]:
        res = []
        comb = []
        end = len(s) - 1

        def partitionHelper(s, start):
            if start > end:
                res.append(comb.copy())
                return
            for i in range(start, end + 1):
                ss = s[start:i + 1]
                if self.isPalindrome(ss):
                    comb.append(ss)
                    partitionHelper(s, i + 1)
                    comb.pop()

        partitionHelper(s, 0)

        return res

    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        comb = []
        ln = len(s) - 1
        dp = [[False for i in range(len(s))] for i in range(len(s))]

        def partitionHelper(s, start):
            if start > ln:
                res.append(comb.copy())
                return
            for i in range(start, ln + 1):
                ss = s[start:i + 1]
                end = i
                if s[start] == s[end] and (end - start + 1 <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    comb.append(ss)
                    partitionHelper(s, i + 1)
                    comb.pop()

        partitionHelper(s, 0)

        return res
