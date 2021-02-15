from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        self.g = defaultdict(list)
        self.disc = [-1 for i in range(n)]
        self.low = [-1 for i in range(n)]
        self.counter = 0
        self.visited = [False for i in range(n)]
        self.bridges = []
        for ed in connections:
            u = ed[0]
            v = ed[1]
            self.g[u].append(v)
            self.g[v].append(u)

        self.dfs(0, None)

        return self.bridges

    def dfs(self, u, parent):
        self.disc[u] = self.low[u] = self.counter
        self.counter += 1
        self.visited[u] = True
        for v in self.g[u]:
            if v == parent:
                continue
            if self.visited[v]:
                self.low[u] = min(self.low[u], self.disc[v])
            else:
                self.dfs(v, u)
                self.low[u] = min(self.low[u], self.low[v])
            if self.low[v] > self.disc[u]:
                self.bridges.append([u, v])


if __name__ == "__main__":
    n = int(input())
    con = []
    for i in range(n):
        temp = list(map(int, input().strip().split()))
        con.append(temp)

    res = Solution().criticalConnections(n, con)
    print(res)
