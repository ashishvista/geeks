from collections import deque
from typing import List


class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1 for i in range(amount + 1)]
        coins.sort()
        for i in coins:
            if i > amount:
                break
            dp[i] = 1

        if dp[amount] == 1:
            return 1

        for i in range(1, amount + 1):
            mn = float("+inf")
            for j in coins:
                if i - j <= 0 or dp[i] == 1:
                    break
                if dp[i - j] > 0:
                    mn = min(dp[i - j] + 1, mn)
                    dp[i] = mn
        return dp[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dq = deque(coins)
        h = {}
        coins.sort()
        for c in coins:
            h[c] = 1
            dq.append(c)
        mxx = (amount // coins[0]) + 1

        while dq:
            item = dq.popleft()
            for c in coins:
                k = c + item
                if k not in h:
                    dq.append(k)
                    h[k] = h[item] + 1
                    if amount in h:
                        return h[amount]
                    if h[item] + 1 >= mxx:
                        return -1


if __name__ == "__main__":
    arr = list(map(int, input().strip()[1:-1].split(",")))
    am = int(input())
    res = Solution().coinChange(arr, am)
    print(res)
