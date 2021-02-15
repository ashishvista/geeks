from collections import defaultdict


class Graph:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def scc(self):
        visited = [False for i in range(self.n)]
        stack = []
        h = {}
        disc = [-1 for i in range(self.n)]
        count = [0]
        for u in self.graph:
            if not visited[u]:
                self.sccUtil(u, visited, stack, disc, h, count)

    def sccUtil(self, u, visited, stack, disc, h, count):
        visited[u] = True
        stack.append(u)
        h[u] = 1
        disc[u] = low = count[0]
        count[0] += 1

        for v in self.graph[u]:
            if not visited[v]:
                vlow = self.sccUtil(v, visited, stack, disc, h, count)
                low = min(vlow, low)
            if visited[v] and v in h:
                low = min(low, disc[v])

        if low == disc[u]:
            scc_arr = []
            item = None
            while item != u:
                item = stack.pop()
                del h[item]
                # print(item, end=" ")
                scc_arr.append(str(item))
            # print()
            s = " ".join(scc_arr) + ","
            print(s, end="")

        return low


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n, m = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        g = Graph(n, m)
        for i in range(n):
            k = g.graph[i]
        for i in range(m):
            g.addEdge(arr[2 * i], arr[2 * i + 1])

        g.scc()
        print()
