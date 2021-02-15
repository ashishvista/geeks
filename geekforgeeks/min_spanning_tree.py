class edges:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


def spanningTree(V, E, graph):
    arr = []
    visited = [[False for j in range(V)] for i in range(V)]
    for i in range(V):
        for j in range(V):
            if graph[i][j] != float('inf') and not visited[i][j]:
                arr.append(edges(i, j, graph[i][j]))
                visited[i][j] = visited[j][i] = True
    arr.sort(key=lambda x: x.w)
    carr = [-1 for i in range(V)]
    sum = 0
    for i in range(V - 1):
        if not detectCyle(arr[i], carr):
            sum += arr[i].w

    return sum
    # print([item.w for item in arr])


def detectCyle(ed, carr):
    u = findParent(ed.u, carr)
    v = findParent(ed.v, carr)

    if u == v:
        return True
    else:
        carr[u] = v
        return False


def findParent(e, carr):
    if carr[e] == -1:
        return e
    else:
        return findParent(carr[e], carr)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        graph = [[float("inf") for i in range(V)] for i in range(V)]
        for i in range(0, len(info), 3):
            u, v, w = info[i] - 1, info[i + 1] - 1, info[i + 2]
            graph[u][v] = w
            graph[v][u] = w
        print(spanningTree(V, E, graph))
