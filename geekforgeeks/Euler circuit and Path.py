from collections import defaultdict
from collections import deque


def isEulerian(g, N, E):
    v = N
    if not isConnected(g, N, E):
        return 0

    oddDegreeVerticesCount = 0

    for v1 in g:
        if len(g[v1]) % 2 != 0:
            oddDegreeVerticesCount += 1

    if oddDegreeVerticesCount == 0:
        return 2
    elif oddDegreeVerticesCount == 2:
        return 1
    else:
        return 0


def isConnected(g, N, E):
    v = N
    visited = [False for i in range(v)]
    q = deque()

    flag = False
    for u in g:
        if g[u] == 0:
            visited[u] = True
        elif len(g[u]) > 0 and not flag:
            q.append(u)
            visited[u] = True
            flag = True

    while q:
        item = q.popleft()
        for c in g[item]:
            if not visited[c]:
                visited[c] = True
                q.append(c)
    if False in visited:
        return False
    return True


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):  # add directed edge from u to v.
        self.graph[u].append(v)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        N, E = map(int, input().strip().split())
        g = Graph(N)
        edges = list(map(int, input().strip().split()))

        for i in range(0, len(edges), 2):
            u, v = edges[i], edges[i + 1]
            g.addEdge(u, v)  # add an undirected edge from u to v
            g.addEdge(v, u)
        print(isEulerian(g.graph, N, E))
