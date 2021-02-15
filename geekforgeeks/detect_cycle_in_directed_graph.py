def isCyclic(n, graph):
    visited = [False for i in range(n)]
    rec = []
    for v in range(n):
        if not visited[v]:
            if dfs(n, graph, visited, rec, v):
                return True
    return False


def dfs(n, graph, visited, rec, v):
    if visited[v] and v in rec:
        return True
    elif visited[v]:
        return False

    visited[v] = True
    rec.append(v)

    for cv in graph[v]:
        if dfs(n, graph, visited, rec, cv):
            return True
    rec.pop()
    return False


def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2


from collections import defaultdict

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa
# } Driver Code Ends
