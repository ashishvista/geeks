import sys
from collections import deque
from typing import List

sys.setrecursionlimit(10000)


class Solution:
    count = float("+inf")

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = {}
        wordListDict = {}
        dp = {}
        hq = {}
        for w in wordList:
            wordListDict[w] = 1
        if endWord not in wordListDict:
            return 0
        wordListDict[beginWord] = 1
        dw = "ands"
        self.ladderLengthHelper(endWord, beginWord, wordListDict, dp, hq, dw)
        if dp[endWord] == float("+inf"):
            return 0
        else:
            print(hq[endWord])
            return dp[endWord]

    def ladderLengthHelper(self, w, beginWord, wordListDict, dp, hq, dw):

        if w == dw:
            print()

        if w in dp and dp[w] != float("inf"):
            return dp[w]

        if w == beginWord:
            dp[w] = 1
            hq[w] = [w]
            return dp[w]

        dp[w] = float("+inf")
        tt = dp[w]
        pw = "aids"
        for i in range(len(w)):
            for j in range(ord("a"), ord("z") + 1):
                ch = chr(j)
                sarr = list(w)
                sarr[i] = ch
                nw = "".join(sarr)
                if w == dw and nw == pw:
                    print()
                    pp = wordListDict[nw]
                    print()
                if nw != w and nw in wordListDict:
                    del wordListDict[nw]
                    if nw == pw:
                        print()
                    res = self.ladderLengthHelper(nw, beginWord, wordListDict, dp, hq, dw) + 1
                    if nw == pw:
                        print()
                    wordListDict[nw] = 1

                    if res < dp[w]:
                        dp[w] = res
                        tmp = hq[nw].copy()
                        tmp.append(w)
                        hq[w] = tmp
                    # dp[w] = min(dp[w], res)
        if w == dw:
            t1 = dp[w]
            print()
        return dp[w]

    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dq = deque([beginWord])
        hq = {beginWord: []}
        wordListDictPattern = {}
        wordListDict = {}
        for w in wordList:
            wordListDict[w] = 1

        for w in wordList:
            for i in range(len(w)):
                sarr = list(w)
                sarr[i] = "*"
                nw = "".join(sarr)
                if nw in wordListDictPattern:
                    wordListDictPattern[nw].append(w)
                else:
                    wordListDictPattern[nw] = [w]

        level = 0
        while dq:
            s = len(dq)
            level += 1
            for k in range(s):
                w = dq.popleft()
                if w == endWord:
                    hq[w].append(w)
                    print(hq[w])
                    return level

                for i in range(len(w)):
                    sarr = list(w)
                    sarr[i] = "*"
                    nw = "".join(sarr)
                    if nw in wordListDictPattern:
                        for ww in wordListDictPattern[nw]:
                            if ww in wordListDict:
                                dq.append(ww)
                                tmp = hq[w].copy()
                                tmp.append(w)
                                hq[ww] = tmp
                                del wordListDict[ww]
                        del wordListDictPattern[nw]
        return 0


if __name__ == "__main__":
    bw = input()[1:-1]
    ew = input()[1:-1]
    wl = list(input()[1:-1].strip().split(","))
    wl = list(map(lambda x: x[1:-1], wl))
    s = Solution().ladderLength(bw, ew, wl)
    print(s)
