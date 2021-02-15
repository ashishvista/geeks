class Graph:
    v = None

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
        self.weights = {}

    def addEdge(self, u, v, w):
        self.adj[u].append(v)
        self.weights[str(u) + "-" + str(v)] = w


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = Graph(N)
        dist = [float("+inf") for i in range(N)]
        dist[K - 1] = 0
        visited = {}
        for uv in times:
            graph.addEdge(uv[0] - 1, uv[1] - 1, uv[2])

        varr = {K - 1: 1}
        while varr:
            su = self.getLowestCostV(varr, dist)
            del varr[su]
            visited[su] = 1
            for v in graph.adj[su]:
                new_dist = dist[su] + graph.weights[str(su) + "-" + str(v)]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                if v not in visited:
                    varr[v] = 1

        largest = float("-inf")
        if len(visited) != N:
            return -1

        for d in dist:
            largest = max(largest, d)
        return largest

    def getLowestCostV(self, varr, dist):
        sw = float("inf")
        sv = None
        for v in varr:
            if sw > dist[v]:
                sw = dist[v]
                sv = v
        return sv
