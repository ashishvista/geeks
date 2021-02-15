import sys

sys.setrecursionlimit(10 ** 6)


def my_except_hook(exctype, value, traceback):
    print(exctype, value, traceback)


sys.excepthook = my_except_hook


# def ncr(n, r, dp):
#     m = 1000000007
#     for i in range(1, n + 1):
#         for j in range(min(i + 1, r + 1)):
#             # if j > i:
#             #     break
#             if j == 0 or i == j:
#                 dp[i][j] = 1
#             else:
#                 dp[i][j] = dp[i - 1][j] % m + dp[i - 1][j - 1] % m
#
#     return dp[n][r]

def ncr(n, r, dp):
    m = 1000000007
    for i in range(0, n + 1):
        for j in range(min(i, r) + 1):
            # if j > i:
            #     break
            if j == 0 or i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j] % m + dp[i - 1][j - 1] % m) % m


def pascal(n, r):
    m = 1000000007
    arr = [1 for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(i - 1, 0, -1):
            arr[j] = arr[j] % m + arr[j - 1] % m
    return arr[r] % m

def binomialCoefficient(n, k):
    res=1
    m = 1000000007

    for i in range(k):
        res=(res  * (n-i) )/(i+1)

    return int(res)



if __name__ == "__main__":
    tcases = int(input())
    dp = [[-1 for i in range(800 + 1)] for i in range(1000 + 1)]
    ncr(1000, 800, dp)
    for t in range(tcases):
        n, r = list(map(int, input().strip().split()))
        if r > n:
            print(0)
        else:
            print(dp[n][r])
        print("pascal-- ", pascal(n, r))
        print("binomialCoefficient-- ", binomialCoefficient(n, r))
