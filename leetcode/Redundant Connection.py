from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.adj = [[] for i in range(v)]
        self.v = v

    def addEdges(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)


class Solution:

    def findRedundantConnection1(self, edges: List[List[int]]) -> List[int]:
        h = {}
        n = float("-inf")
        for ed in edges:
            n = max(ed[0], ed[1], n)

        n = n + 1
        g = Graph(n)

        for ed in edges:
            visited = {}
            g.addEdges(ed[0], ed[1])
            if self.isCyclic(g, ed[0], None, visited):
                return ed

        return []

    def isCyclic1(self, g, u, parent, visited):
        if u in visited:
            return False

        visited[u] = 1
        for v in g.adj[u]:
            if v in visited and parent != v:
                return True
            res = self.isCyclic(g, v, u, visited)
            if res:
                return True

        return False

    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
        g = defaultdict(set)

        for ed in edges:
            visited = {}
            if self.isCyclic(g, ed[0], ed[1], visited):
                return ed
            g[ed[0]].add(ed[1])
            g[ed[1]].add(ed[0])

        return []

    def isCyclic2(self, g, u, target, visited):
        if u in visited:
            return False

        visited[u] = 1
        for v in g[u]:
            if v == target:
                return True
            res = self.isCyclic(g, v, target, visited)
            if res:
                return True

        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        h = {}
        for ed in edges:
            l = self.getSet(ed[0], h)
            r = self.getSet(ed[1], h)
            if l == r:
                return ed
            h[l] = r
        return []   

    def getSet(self, u, h):
        if u in h:
            return self.getSet(h[u], h)
        else:
            return u
