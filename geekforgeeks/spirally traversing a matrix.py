import sys


def my_except_hook(exctype, value, traceback):
    print("hello")


sys.excepthook = my_except_hook


def spiral(arr, m, n):
    # order = ["right", "down", "left", "up"]
    order = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited = [[False for i in range(n)] for i in range(m)]
    count = m * n
    x = 0
    y = 0
    cur = 0
    while True:
        if count < 1:
            break;
        if x >= 0 and y >= 0 and x < m and y < n and not visited[x][y]:
            tmp = arr[x][y]
            print(arr[x][y], end=" ")
            visited[x][y] = True
            count -= 1
        else:
            x -= order[cur][0]
            y -= order[cur][1]
            cur += 1
            cur = cur % 4
        x += order[cur][0]
        y += order[cur][1]


def spiral2(arr, i, j, m, n, tt):
    # print 1st row
    if i > m - 1 or j > n - 1:
        return
    for k in range(j, n):
        print(arr[i][k], end=" ")
        tt.append(arr[i][k])

    # last column
    for k in range(i + 1, m):
        print(arr[k][n - 1], end=" ")
        tt.append(arr[k][n - 1])

    # last row
    if i != m - 1:
        for k in range(n - 2, j - 1, -1):
            print(arr[m - 1][k], end=" ")
            tt.append(arr[m - 1][k])

    # first column
    if j != n - 1:
        for k in range(m - 2, i, -1):
            print(arr[k][j], end=" ")
            tt.append(arr[k][j])

    spiral2(arr, i + 1, j + 1, m - 1, n - 1, tt)


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        m, n = list(map(int, input().strip().split()))
        tmp = list(map(int, input().strip().split()))
        c = 0
        arr = []

        for i in range(m):
            p = []
            for j in range(n):
                p.append(tmp[c])
                c += 1
            arr.append(p)
        # spiral(arr, m, n)
        # print()
        tt = []
        spiral2(arr, 0, 0, m, n, tt)
        print()
