class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.transposedGraph = defaultdict(list)

    def getvisitedFinishTime(self, u):
        self.visited[u] = True
        for v in self.graph[u]:
            if not self.visited[v]:
                self.getvisitedFinishTime(v)
        self.stackFinish.append(u)

    def scc(self):
        self.visited = [False for i in range(self.n)]
        self.stackFinish = []
        for u in range(self.n):
            if not self.visited[u]:
                self.getvisitedFinishTime(u)
        self.transpose()
        self.visited = [False for i in range(self.n)]
        count = 0
        stLen = len(self.stackFinish)
        while self.stackFinish:
            u = self.stackFinish.pop()
            if not self.visited[u]:
                count += 1
                self.dfs(u)
        return count

    def transpose(self):
        for u in self.graph:
            for v in self.graph[u]:
                self.transposedGraph[v].append(u)

    def dfs(self, u):
        self.visited[u] = True
        for v in self.transposedGraph[u]:
            if not self.visited[v]:
                self.dfs(v)


def countSCCs(graph, V):
    g = Graph(V)
    g.graph = graph
    return g.scc()


import sys

sys.setrecursionlimit(10 ** 6)


def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        i += 2


from collections import defaultdict

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        print(countSCCs(graph, n))
