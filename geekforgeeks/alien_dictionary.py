# User function Template for python3
import sys

from collections import defaultdict

ad = None
nn = None
k = None
gg=None

def my_except_hook(exctype, value, traceback):
    print(ad, nn, k)


# sys.excepthook = my_except_hook


def printOrder(alien_dict, n, k):
    graph = defaultdict(list)
    c = 0
    while c < len(alien_dict) - 1:
        str1 = alien_dict[c]
        str2 = alien_dict[c + 1]
        m = min(len(str1), len(str2))
        d = 0
        while d < m:
            if str1[d] == str2[d]:
                d += 1
                continue
            else:
                graph[str1[d]].append(str2[d])
                break
        c += 1
    global ad
    ad = alien_dict
    global nn
    nn = n
    global kk
    kk = k
    global gg
    gg=graph
    # print(alien_dict, n, k, graph)

    for w in alien_dict:
        for c in w:
            if c  not in graph:
                graph[c]=[]

    order = topoSort(graph)
    # print(order)
    return order


def topoSort(graph):
    visited = {}
    order = []
    keys = list(graph.keys())
    for node in keys:
        if node not in visited:
            visited[node] = 1
            topSortutil(node, graph, order, visited)
            order.append(node)
    order.reverse()
    return order


def topSortutil(node, graph, order, visited):
    for child in graph[node]:
        if child not in visited:
            visited[child] = 1
            topSortutil(child, graph, order, visited)
            order.append(child)


# code here
# return the string containing all k characters in correct order


# {
#  Driver Code Starts
# Initial Template for Python 3

class sort_by_order:
    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])

        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()

        order = printOrder(alien_dict, n, k)

        x = sort_by_order(order)
        x.sort_this_list(duplicate_dict)

        if duplicate_dict == alien_dict:
            print(1)
        else:
            print(0)

# } Driver Code Ends
