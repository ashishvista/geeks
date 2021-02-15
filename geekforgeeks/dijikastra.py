# User function Template for python3

'''
src - starting node of graph (int)
V - number of vertices (int)
graph - 2d list represeting graph contains weight

'''


class node:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


def dijkstra(src, V, graph):
    visited = [False for i in range(V)]
    visited[src] = True
    dist = [float('inf') for i in range(V)]
    dist[src] = 0
    arr = [node(src, src, graph[src][src])]
    temp = []

    while len(arr) > 0:
        u = arr.pop(0).v

        for v in range(V):
            if graph[u][v] == 0:
                continue
            d = dist[u] + graph[u][v]
            if d < dist[v]:
                dist[v] = d
            if not visited[v]:
                temp.append(node(u, v, dist[v]))
                visited[v] = True

        if len(arr) == 0 and len(temp) > 0:
            temp.sort(key=lambda x: x.w)
            arr = temp
            temp = []
    for i in dist:
        print(i,end=' ')
    print()


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for tst in range(t):
        v = int(input())
        graph = [[0 for column in range(v)]
                 for row in range(v)]

        lst = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(v):
            for j in range(v):
                graph[i][j] = lst[k]
                k += 1
        s = int(input())
        dijkstra(s, v, graph)

# } Driver Code Ends
