from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        si2 = 0
        si1 = 0
        bi1 = -prices[0]
        for i in range(1, n):
            cur = prices[i]
            curB = max(si2 - cur, bi1)
            curs = max(bi1 + cur, si1)
            bi1 = curB
            si2 = si1
            si1 = curs

        return si1


if __name__ == "__main__":
    arr = list(map(int, input().strip()[1:-1].split(",")))
    s = Solution().maxProfit(arr)
    print(s)
