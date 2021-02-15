from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n
        self.rec = []
        self.visited = [False for i in range(self.n)]

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isHam(self):
        for i in range(self.n):
            if self.dfs(i):
                return 1
        return 0

    def dfs(self, v):

        if self.visited[v]:
            return False

        self.visited[v] = True
        self.rec.append(v)
        # if len(self.rec) >8:
        #     print(self.rec)

        if len(self.rec) == self.n:
            return True

        for cv in self.graph[v]:
            if self.dfs(cv):
                return True
        self.visited[v] = False
        self.rec.pop()


if __name__ == "__main__":
    tcase = int(input())
    for i in range(tcase):
        n, m = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        g = Graph(n)
        k = 0
        for j in range(m):
            g.addEdge(arr[k]-1, arr[k + 1]-1)
            k += 2
        # print(g.graph)
        print(g.isHam())
