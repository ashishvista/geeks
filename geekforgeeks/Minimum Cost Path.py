from collections import deque


def min_cost(arr, n):
    dist = [[float("inf") for i in range(n)] for i in range(n)]
    visited = [[False for i in range(n)] for i in range(n)]
    points = deque()
    points.append([0, 0])
    visited[0][0] = True
    dist[0][0] = arr[0][0]
    directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    while points:
        i = findMin(points, dist)
        item = points[i]
        x = item[0]
        y = item[1]
        del points[i]

        for d in directions:
            p = x + d[0]
            q = y + d[1]
            if 0 <= p < n and 0 <= q < n:
                if not visited[p][q]:
                    points.append([p, q])
                    visited[p][q] = True
                dist[p][q] = min(dist[x][y] + arr[p][q], dist[p][q])
    return dist[n - 1][n - 1]


def findMin(points, dist):
    if not points:
        return -1
    x = points[0][0]
    y = points[0][1]
    minv = dist[x][y]
    mini = 0
    for i, point in enumerate(points):
        x = point[0]
        y = point[1]
        if dist[x][y] < minv:
            minv = dist[x][y]
            mini = i
    return mini


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        tmp = list(map(int, input().strip().split()))
        c = 0
        arr = []
        for i in range(n):
            temp2 = []
            for j in range(n):
                temp2.append(tmp[c])
                c += 1
            arr.append(temp2)
        res = min_cost(arr, n)
        print(res)
