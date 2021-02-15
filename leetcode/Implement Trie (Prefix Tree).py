class TrieNode:
    link = None
    wordEnd = False

    def __init__(self):
        self.link = [None for i in range(26)]

    def setWordEnd(self):
        self.wordEnd = True


class Trie:
    root = None

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        t = self.root
        for ch in word:
            pos = ord(ch) - ord('a')
            if t.link[pos] is None:
                t.link[pos] = TrieNode()
            t = t.link[pos]
        t.setWordEnd()

    def search(self, word: str) -> bool:
        t = self.root
        for ch in word:
            pos = ord(ch) - ord('a')
            if t.link[pos] is None:
                return False
            t = t.link[pos]

        if t.wordEnd:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        t = self.root
        for ch in prefix:
            pos = ord(ch) - ord('a')
            if t.link[pos] is None:
                return False
            t = t.link[pos]
        return t


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    T = Trie()
    x = T.startsWith("a")
    T.insert("ashish")
    print()
