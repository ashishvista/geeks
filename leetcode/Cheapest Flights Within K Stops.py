from collections import defaultdict, deque


class Node:
    def __init__(self, v, w):
        self.v = v
        self.w = w


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        self.g = defaultdict(list)
        for ed in flights:
            u = ed[0]
            v = ed[1]
            w = ed[2]
            self.g[u].append(Node(v, w))

        self.mnn = float("+inf")
        self.n = n
        self.src = src
        self.dst = dst
        self.K = K
        self.visited = {}
        self.visited[self.src] = 0
        self.bfs(self.src)

        if self.dst not in self.visited:
            return -1
        else:
            return self.visited[self.dst]

    def bfs(self, u):
        q = deque()
        q.append(u)
        k = 0
        while q and k <= self.K:
            c = len(q)
            curvisit = {}
            while c > 0:
                u = q.popleft()
                for node in self.g[u]:
                    v = node.v
                    w = node.w
                    nw = self.visited[u] + w
                    if (v in self.visited and nw < self.visited[v]) or v not in self.visited:
                        if v in curvisit:
                            curvisit[v] = min(nw, curvisit[v])
                        else:
                            curvisit[v] = nw
                        if v not in self.visited:
                            self.visited[v] = nw
                        if v != self.dst:
                            q.append(v)

                c -= 1
            for v in curvisit:
                self.visited[v] = curvisit[v]
            k += 1
