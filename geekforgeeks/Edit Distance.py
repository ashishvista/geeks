from collections import deque


def editDistance(m, n, s1, s2):
    dp = [[0 for i in range(m + 1)] for i in range(n + 1)]
    dp_index = []
    for i in range(n + 1):
        tmp = []
        for j in range(m + 1):
            tmp.append([])
        dp_index.append(tmp)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[j - 1] == s2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                tmp = cpy(dp_index, i - 1, j - 1)
                tmp.append([i - 1, j - 1])
                dp_index[i][j] = tmp
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    dp_index[i][j] = cpy(dp_index, i - 1, j)
                else:
                    dp[i][j] = dp[i][j - 1]
                    dp_index[i][j] = cpy(dp_index, i, j - 1)

    x = deque(dp_index[n][m])
    x.appendleft([-1, -1])
    x.append([n, m])

    l = len(x) - 1
    index = 0
    tot = 0
    while index < l:
        t1 = x[index + 1][0] - x[index][0] - 1
        t2 = x[index + 1][1] - x[index][1] - 1
        tot += max(t1, t2)
        index += 1

    print(tot)


def cpy(dp_index, i, j):
    arr = []

    for a in dp_index[i][j]:
        tmp = a.copy()
        arr.append(tmp)

    if arr is None:
        print()
    return arr


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        m, n = list(map(int, input().strip().split()))
        s1, s2 = list(input().strip().split())
        editDistance(m, n, s1, s2)
