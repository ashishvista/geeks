def countGroups(related):
    n = len(related)
    for i in range(n):
        tmp = related[i]
        arr = [int(j) for j in tmp]
        related[i] = arr
    matrix = createAdjacenyMartrix(related, n)
    res = countTrees(matrix, n)
    return res


def createAdjacenyMartrix(related, n):
    matrix = [[] for i in range(n)]
    c = len(related[0])
    for i in range(n):
        for j in range(c):
            if i != j and related[i][j] == 1:
                matrix[i].append(j)
    return matrix


def DFSUtil(u, adj, visited):
    visited[u] = True
    for i in range(len(adj[u])):
        if (visited[adj[u][i]] == False):
            DFSUtil(adj[u][i], adj, visited)


def countTrees(adj, V):
    visited = [False] * V
    res = 0
    for u in range(V):
        if (visited[u] == False):
            DFSUtil(u, adj, visited)
            res += 1
    return res


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        tmp = input()
        arr.append(tmp)
    res = countGroups(arr)
    print(res)
