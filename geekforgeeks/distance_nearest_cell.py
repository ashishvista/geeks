from collections import deque


#
# def distance(m, n, arr):
#     dist = [[float("inf") for i in range(n)] for i in range(m)]
#     for x in range(m):
#         for y in range(n):
#             visited = [[False for i in range(n)] for i in range(m)]
#             q = deque()
#             q.append([x, y, 0])
#             visited[x][y] = True
#             while q:
#                 item = q.popleft()
#                 i = item[0]
#                 j = item[1]
#                 d = item[2]
#                 if arr[i][j] == 1:
#                     dist[x][y] = d
#                     break
#
#                 if isSafe(arr, visited, m, n, i, j - 1):
#                     q.append([i, j - 1, d + 1])
#                     visited[i][j - 1] = True
#
#                 if isSafe(arr, visited, m, n, i - 1, j):
#                     q.append([i - 1, j, d + 1])
#                     visited[i - 1][j] = True
#
#                 if isSafe(arr, visited, m, n, i, j + 1):
#                     q.append([i, j + 1, d + 1])
#                     visited[i][j + 1] = True
#
#                 if isSafe(arr, visited, m, n, i + 1, j):
#                     q.append([i + 1, j, d + 1])
#                     visited[i + 1][j] = True
#     print(dist)


def distance2(m, n, arr, visited, dist, q, t):
    # if m < 1 or n < 1:
    #     print("worng")
    #     return
    # if t==18:
    #     print("hello")
    #     return
    # visited = [[False for i in range(n)] for i in range(m)]
    # dist = [[float("inf") for i in range(n)] for i in range(m)]

    # q = deque()
    # for i in range(m):
    #     for j in range(n):
    #         if arr[i][j] == 1:
    #             visited[i][j] = True
    #             q.append([i, j, 0])
    # print("", q)
    while q:
        item = q.popleft()
        i = item[0]
        j = item[1]
        d = item[2]
        dist[i][j] = d

        if isSafe(arr, visited, m, n, i, j - 1):
            q.append([i, j - 1, d + 1])
            visited[i][j - 1] = True

        if isSafe(arr, visited, m, n, i - 1, j):
            q.append([i - 1, j, d + 1])
            visited[i - 1][j] = True

        if isSafe(arr, visited, m, n, i, j + 1):
            q.append([i, j + 1, d + 1])
            visited[i][j + 1] = True

        if isSafe(arr, visited, m, n, i + 1, j):
            q.append([i + 1, j, d + 1])
            visited[i + 1][j] = True

    for i in range(m):
        for j in range(n):
            print(dist[i][j], end=" ")

    print()


def isSafe(arr, visited, m, n, i, j):
    # if i < 0 or i >= m or j < 0 or j >= n or visited[i][j]:
    #     return False
    if i >= 0 and i < m and j >= 0 and j < n and not visited[i][j]:
        return True
    return False


# def isSafe2(arr, m, n, i, j):
#     if i < 0 or i >= m or j < 0 or j >= n:
#         return False
#     return True
#
#
# def distance3(m, n, arr):
#     g = createGraph(m, n, arr)
#     dist = [float("inf") for i in range(m * n)]
#     visited = [False for i in range(m * n)]
#     q = deque()
#
#     for i in range(m):
#         for j in range(n):
#             if arr[i][j] == 1:
#                 v = n * i + j
#                 q.append(v)
#                 visited[v] = True
#                 dist[v] = 0
#
#     while q:
#         v1 = q.popleft()
#         for v2 in g[v1]:
#             if not visited[v2]:
#                 q.append(v2)
#                 visited[v2] = True
#                 dist[v2] = dist[v1] + 1
#     for d in dist:
#         print(d, end=" ")
#     print()


# def createGraph(m, n, arr):
#     g = {}
#     directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
#     for i in range(m):
#         for j in range(n):
#             v = i * n + j
#             g[v] = []
#             for k in directions:
#                 x, y = [i + k[0], j + k[1]]
#                 if isSafe2(arr, m, n, x, y):
#                     g[v].append(x * n + y)
#     return g


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        m, n = list(map(int, input().strip().split()))
        temp = list(map(int, input().strip().split()))
        # temp = [random.randint(1,1) for _ in range(m * n)]
        arr = []
        visited = []
        dist = []
        c = 0
        q = deque()
        for i in range(m):
            tmp = []
            vtmp = []
            dtmp = []
            for j in range(n):
                if temp[c] == 1:
                    vtmp.append(True)
                    q.append([i, j, 0])
                else:
                    tmp.append(temp[c])
                    vtmp.append(False)
                tmp.append(temp[c])
                dtmp.append(float("inf"))
                c = c + 1
            arr.append(tmp)
            visited.append(vtmp)
            dist.append(dtmp)
        # distance(m, n, arr)  ## brute force bfs
        distance2(m, n, arr, visited, dist, q, t)  ## multisource bfs directly on matrix
        # distance3(m, n, arr)  ### create graph then multisource bfs
