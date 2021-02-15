# def paths(m, n):
#     return go(0, 0, m, n)
#
#
# def go(x, y, m, n):
#     if x == m - 1 and y == n - 1:
#         return 1
#     elif not issafe(x, y, m, n):
#         return 0
#     else:
#         res = go(x + 1, y, m, n) + go(x, y + 1, m, n)
#         return res
#
#
# def issafe(x, y, m, n):
#     if x <= m - 1 and y <= n - 1:
#         return True
#     else:
#         return False

def paths2(m, n):
    dp = [[0 for i in range(n)] for i in range(m)]
    for i in range(n):
        dp[m - 1][i] = 1
    for i in range(m):
        dp[i][n - 1] = 1

    for i in range(m - 2, 0 - 1, -1):
        for j in range(n - 2, 0 - 1, -1):
            dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
    return dp[0][0]


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        m, n = list(map(int, input().strip().split()))
        # print(paths(m, n))
        print(paths2(m, n))
