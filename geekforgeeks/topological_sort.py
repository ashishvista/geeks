# Your task is to complete this function
# Function should return Topologically Sorted List
# Graph(graph) is a defaultict of type List
# n is no of edges
from collections import defaultdict

def topoSort(n, graph):
    # Code here
    visited = [False for i in range(n)]
    res = []
    for i in range(n):
        if not visited[i]:
            topoSortUtil(i, graph, visited, res)
    res.reverse()
    return res


def topoSortUtil(i, graph, visited, res):
    visited[i] = True
    for k in graph[i]:
        if not visited[k]:
            topoSortUtil(k, graph, visited,res)
    res.append(i)


# {
#  Driver Code Starts
# Driver Program
def creategraph(e, n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        i += 2



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        e, N = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, N, arr, graph)
        res = topoSort(N, graph)
        # print res
        valid = True
        for i in range(N):
            n = len(graph[res[i]])
            for j in range(len(graph[res[i]])):
                for k in range(i + 1, N):
                    if res[k] == graph[res[i]][j]:
                        n -= 1
            # print n
            if n != 0:
                valid = False
                break
        if valid:
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends
