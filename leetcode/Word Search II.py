from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        dir = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        visited = [[False for i in range(n)] for i in range(m)]
        ewords = set()

        trie = self.createTrie(words)
        r = self.wordExists(trie, "oath")

        for i in range(m):
            for j in range(n):
                self.findWordsHelper(board, m, n, i, j, visited, dir, trie, ewords, "")

        return list(ewords)

    def isValid(self, m, n, i, j):
        if i >= 0 and i < m and j >= 0 and j < n:
            return True
        return False

    def findWordsHelper(self, board, m, n, i, j, visited, dir, trie, ewords, s):
        visited[i][j] = True
        s = s + board[i][j]

        t = trie
        ch = ord(board[i][j]) - 97

        if t[ch]:
            t = t[ch]
            if t[26]:
                ewords.add(t[27])
        else:
            visited[i][j] = False
            return

        for d in dir:
            x = i + d[0]
            y = j + d[1]
            if self.isValid(m, n, x, y) and not visited[x][y]:
                self.findWordsHelper(board, m, n, x, y, visited, dir, t, ewords, s)

        visited[i][j] = False

    def createTrie(self, words):
        trie = [None for i in range(28)]
        # trie[26] = False
        for w in words:
            t = trie
            for ch in w:
                index = ord(ch) - 97
                if not t[index]:
                    t[index] = [None for i in range(28)]
                    t[index][26] = False
                t = t[index]
            t[26] = True
            t[27] = w
        return trie

    def wordExists(self, trie, word):
        t = trie
        for ch in word:
            index = ord(ch) - 97
            if t[index]:
                t = t[index]
            else:
                return False
        if t[26]:
            return True
        else:
            return False


if __name__ == "__main__":
    arr = []
    n = int(input())
    for i in range(n):
        arr.append(list(input().strip().split()))
    w = list(input().strip().split())
    s = Solution().findWords(arr, w)
    print(s)


# if __name__ == "__main__":
#     w = list(input().strip().split())
#     s = Solution()
#     t = s.createTrie(w)
#     res = s.wordExists(t, "aa")
#     print(res)
