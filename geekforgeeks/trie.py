class Node:
    def __init__(self):
        self.child = [None for i in range(26)]
        self.leaf = False
        self.str = None


class Trie:
    def __init__(self):
        self.root = Node()

    def addWordToTrie(self, s):
        self.addWordToTrieUtil(self.root, s, 0)

    def addWordToTrieUtil(self, node, s, i):
        ch = s[i].lower()
        index = ord(ch) - 97
        if not node.child[index]:
            child = Node()
            node.child[index] = child
        if i == len(s) - 1:
            node.child[index].leaf = True
            node.child[index].str = s
            return
        self.addWordToTrieUtil(node.child[index], s, i + 1)

    def search(self, s):
        return self.searchUtil(self.root, s, 0)

    def searchUtil(self, node, s, i):
        if i == len(s):
            return True
        if s[i] not in node:
            return False
        else:
            return self.searchUtil(node[s[i]], s, i + 1)


def boggleTrie(m, n, arr, trie):
    directions = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    visited = [[False for i in range(n)] for i in range(m)]
    h = {}
    h_arr = []
    for i in range(m):
        for j in range(n):
            ch = arr[i][j].lower()
            index = ord(ch) - 97
            root = trie.root
            ch_arr = []
            if root.child[index]:
                dfsUtil(m, n, arr, i, j, directions, visited, trie, root.child[index], ch_arr, h, h_arr)
    h_arr.sort()
    if not h_arr:
        print(-1, end=" ")
    for i in h_arr:
        print(i, end=" ")


def dfsUtil(m, n, arr, i, j, directions, visited, trie, node, ch_arr, h, h_arr):
    visited[i][j] = True
    ch_arr.append(arr[i][j])

    if node.leaf:
        strr = ""
        strr = strr.join(ch_arr)
        if strr not in h:
            h[strr] = 1
            h_arr.append(strr)

    for index, child in enumerate(node.child):
        if child is not None:
            for d in directions:
                x = i + d[0]
                y = j + d[1]
                if isSafe(x, y, m, n, arr, visited) and (ord(arr[x][y].lower()) - 97) == index:
                    dfsUtil(m, n, arr, x, y, directions, visited, trie, node.child[index], ch_arr, h, h_arr)

    ch_arr.pop()
    visited[i][j] = False


def isSafe(x, y, m, n, arr, visited):
    if x >= 0 and x < m and y >= 0 and y < n and not visited[x][y]:
        return True
    else:
        False


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        k = int(input())
        str_arr = input().strip().split(" ")
        m, n = list(map(int, input().strip().split()))
        temp = input().strip().split()
        c = 0
        arr = []
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(temp[c])
                c += 1
            arr.append(tmp)
        trie = Trie()
        for s in str_arr:
            trie.addWordToTrie(s)
        boggleTrie(m, n, arr, trie)

        print()

# ord("a") -97
