class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.unsafe = set()
        self.visited = set()
        self.g = graph
        self.safe = set()

        for i in range(len(graph)):
            self.safe.add(i)

        for u, varr in enumerate(self.g):
            if u not in self.visited:
                self.st = set()
                self.dfs(u)

        return self.safe

    def dfs(self, u):

        self.visited.add(u)
        self.st.add(u)

        for v in self.g[u]:
            if v in self.st or v in self.unsafe:
                for p in self.st:
                    self.unsafe.add(p)
                    self.safe.discard(p)
            elif v not in self.visited:
                self.dfs(v)

        self.st.remove(u)
