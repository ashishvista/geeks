import math


def path_in_matrix(n, arr):
    dp = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        dp[0][i] = arr[0][i]

    for i in range(1, n):
        for j in range(n):
            a = dp[i - 1][j - 1] if isValid(i - 1, j - 1, n) else 0
            b = dp[i - 1][j] if isValid(i - 1, j, n) else 0
            c = dp[i - 1][j + 1] if isValid(i - 1, j + 1, n) else 0
            dp[i][j] = max(a, b, c) + arr[i][j]

    maxx = float("-inf")
    for i in range(n):
        if maxx < dp[n - 1][i]:
            maxx = dp[n - 1][i]

    return maxx


def isValid(i, j, n):
    if i >= 0 and j >= 0 and i < n and j < n:
        return True
    else:
        return False


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        tmp = list(map(int, input().strip().split()))
        arr = []
        c = 0
        for i in range(n):
            t = []
            for j in range(n):
                t.append(tmp[c])
                c += 1
            arr.append(t)
        res=path_in_matrix(n, arr)
        print(res)

