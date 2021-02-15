from collections import defaultdict


class Graph:
    def __init__(self, N):
        self.graph = defaultdict(list)
        self.N = N

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s, d):
        visited = [False for i in range(self.N * self.N)]
        q = [s]
        visited[s] = True
        while q:
            c = q.pop(0)
            for i in self.graph[c]:
                if i == d:
                    return 1
                elif not visited[i]:
                    q.append(i)
                    visited[i] = True
        return 0


def isPathExists(mat, N):
    s, d = None, None
    g = Graph(N)
    k = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] != 0:
                if isSafe(N, mat, i, j - 1):
                    g.addEdge(k, k - 1)
                if isSafe(N, mat, i, j + 1):
                    g.addEdge(k, k + 1)
                if isSafe(N, mat, i - 1, j):
                    g.addEdge(k, k - N)
                if isSafe(N, mat, i + 1, j):
                    g.addEdge(k, k + N)

            if mat[i][j] == 1:
                s = k
            elif mat[i][j] == 2:
                d = k
            k += 1

    # print("\n")
    # for i in range(N):
    #     print(mat[i])
    # print(g.graph)
    print(g.bfs(s, d))


def isSafe(N, mat, i, j):
    if i >= 0 and i < N and j >= 0 and j < N and mat[i][j] != 0:
        return True
    else:
        return False


if __name__ == '__main__':
    tcase = int(input())
    for t in range(tcase):
        N = int(input())
        arr = list(map(int, input().strip().split()))
        mat = []
        k = 0
        for i in range(N):
            tmp = []
            for j in range(N):
                tmp.append(arr[k])
                k += 1
            mat.append(tmp)
        isPathExists(mat, N)
