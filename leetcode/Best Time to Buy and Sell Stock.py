from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or n == 1:
            return 0
        maxx = [0 for i in range(n)]
        maxx[n - 1] = prices[n - 1]
        for i in range(n - 2, -1, -1):
            if prices[i] > maxx[i + 1]:
                maxx[i] = prices[i]
            else:
                maxx[i] = maxx[i + 1]

        mx = 0
        for i in range(n):
            tmp = maxx[i] - prices[i]
            mx = max(mx, tmp)

        return mx

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or n == 1:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for i in range(n):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)
        return maxProfit


if __name__ == "__main__":
    arr = list(map(int, input()[1:-1].strip().split(",")))
    s = Solution()
    res = s.maxProfit(arr)
    print(res)
