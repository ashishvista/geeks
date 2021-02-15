def isBridge(graph, n, u, v):
    bridges = findAllBridges(graph, n)
    for bridge in bridges:
        if (u == bridge[0] and v == bridge[1]) or (v == bridge[0] and u == bridge[1]):
            return True
    return False


def findAllBridges(graph, n):
    visited = [False for i in range(n)]
    disc = [-1 for i in range(n)]
    count = [-1]
    bridges = []
    articulation_points = []
    for u in graph:
        findAllBridgesUtil(u, graph, n, visited, count, None, disc, bridges, articulation_points)

    return bridges


def findAllBridgesUtil(u, graph, n, visited, count, parent, disc, bridges, articulation_points):
    visited[u] = True
    count[0] += 1
    disc[u] = low = count[0]
    children = 0

    for v in graph[u]:
        if not visited[v]:
            children += 1
            vlow = findAllBridgesUtil(v, graph, n, visited, count, u, disc, bridges, articulation_points)
            low = min(low, vlow)
            if vlow > disc[u]:
                bridges.append([u, v])
            elif parent is not None and vlow >= disc[u]:
                articulation_points.append(u)
            elif parent is None and children > 1:
                articulation_points.append(u)
        elif visited[v] and parent != v:
            low = min(disc[v], low)
    return low


####################################################################
# def isBridge(graph, n, u, v):
#     graph[u].remove(v)
#     graph[v].remove(u)
#
#     visited = [False for i in range(n)]
#     dfs(graph, n, u, visited)
#     if visited[v]:
#         return False
#     else:
#         return True


# def dfs(graph, n, u, visited):
#     visited[u] = True
#     for v in graph[u]:
#         if not visited[v]:
#             dfs(graph, n, v, visited)


#############################################
def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        graph[arr[i + 1]].append(arr[i])
        i += 2


from collections import defaultdict

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        u, v = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isBridge(graph, n, u, v):
            print(1)
        else:
            print(0)
