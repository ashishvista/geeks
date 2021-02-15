# User function Template for python3
def isCyclic(g, n):
    visited = [False for i in range(n)]
    for v in range(n):
        if not visited[v]:
            if dfs(g, n, visited, v, -1):
                return 1
    return 0


def dfs(g, n, visited, v, p):
    visited[v] = True
    for cv in g[v]:
        if not visited[cv]:
            if dfs(g, n, visited, cv, v):
                return True
        elif cv != p:
            return True
    return False


from collections import defaultdict


# Contributed by : Nagendra Jha

# Graph Class:
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
        print(isCyclic(g.graph, N))
# } Driver Code Ends
