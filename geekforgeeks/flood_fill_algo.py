def FloodFill(arr, m, n, x, y, k):
    visited = [[False for i in range(n)] for i in range(m)]
    c = arr[x][y]
    fill(arr, m, n, x, y, c, k, visited)
    for i in range(m):
        for j in range(n):
            print(arr[i][j], end=" ")
    return 0


def fill(arr, m, n, x, y, c, k, visited):
    if not isSafe(arr, m, n, x, y):
        return
    if visited[x][y] == True:
        return
    visited[x][y] = True
    if arr[x][y] != c:
        return
    arr[x][y] = k
    fill(arr, m, n, x + 1, y, c, k, visited)
    fill(arr, m, n, x, y + 1, c, k, visited)
    fill(arr, m, n, x - 1, y, c, k, visited)
    fill(arr, m, n, x, y - 1, c, k, visited)


def isSafe(arr, m, n, x, y):
    if x >= 0 and x < m and y >= 0 and y < n:
        return True
    else:
        return False


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        m, n = list(map(int, input().strip().split()))
        arr = [[0 for i in range(n)] for i in range(m)]
        values = list(map(int, input().strip().split()))
        c = 0
        for i in range(m):
            for j in range(n):
                arr[i][j] = values[c]
                c += 1
        x, y, k = list(map(int, input().strip().split()))
        FloodFill(arr, m, n, x, y, k)
        print()
