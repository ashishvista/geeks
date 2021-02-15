from collections import defaultdict


class Node:
    def __init__(self, si, pi):
        self.si = si
        self.pi = pi


class Solution:
    def isMatch1(self, s: str, p: str) -> bool:
        self.g = defaultdict(list)
        self.ns = len(s)
        self.np = len(p)

        if s == "":
            for ch in p:
                if ch != "*":
                    return False
            return True

        for i, ch in enumerate(s):
            self.g[ch].append(i)

        st = []

        st.append(Node(-1, -1))

        while st:
            item = st.pop()

            si = item.si + 1
            pi = item.pi + 1

            while si < self.ns and pi < self.np:

                if p[pi] == "?" or p[pi] == "." or s[si] == p[pi]:
                    si += 1
                    pi += 1
                    continue

                elif p[pi] == "*":
                    while pi + 1 < self.np and p[pi + 1] == "*":
                        pi += 1

                    if pi + 1 == self.np:
                        return True

                    pch = p[pi + 1]
                    lst_indexes = self.g[pch]
                    if pch == "?" or pch == ".":
                        for index in range(self.ns - 1, si - 1, -1):
                            st.append(Node(index, pi + 1))
                    else:
                        for i in range(len(lst_indexes) - 1, -1, -1):
                            index = lst_indexes[i]
                            if index >= si:
                                st.append(Node(index, pi + 1))
                            else:
                                break

                    break
                else:
                    break

            if si == self.ns:
                if pi == self.np:
                    return True
                else:
                    for i in range(pi, self.np):
                        ch = p[i]
                        if ch != "*":
                            return False
                    return True

        return False

    def isMatch2(self, s: str, p: str) -> bool:
        sn = len(s)
        pn = len(p)

        if s == "":
            for ch in p:
                if ch != "*":
                    return False
            return True

        dp = [[True for i in range(sn + 1)] for i in range(pn + 1)]

        dp[0][0] = True

        def printdp():
            for i in range(pn + 1):
                for j in range(sn + 1):
                    print(dp[i][j], " ", end="")
                print()

        for i in range(1, sn + 1):
            dp[0][i] = False

        for i in range(1, pn + 1):
            dp[i][0] = False

        previouslowestindex = 1

        if pn > 0 and p[0] == "*":
            dp[1][0] = True

        for i in range(1, pn + 1):
            flag = False
            currlowestindex = None
            for j in range(1, sn + 1):
                sch = s[j - 1]
                pch = p[i - 1]
                if pch == "*":
                    if i - 1 >= 0 and dp[i - 1][0]:
                        dp[i][0] = True
                    currlowestindex = previouslowestindex
                    for k in range(1, previouslowestindex):
                        dp[i][k] = False
                    flag = True
                    break
                elif pch == "?" and i - 2 >= 0 and p[i - 2] == "*" and j > previouslowestindex:
                    if not flag:
                        currlowestindex = j
                    flag = True
                    break
                elif (pch == "?" or sch == pch) and dp[i - 1][j - 1]:
                    if not flag:
                        currlowestindex = j
                    flag = True
                    continue
                else:
                    dp[i][j] = False

            previouslowestindex = currlowestindex
            if not flag:
                # printdp()
                return False

        # printdp()
        return dp[pn][sn]

    def isMatch(self, s: str, p: str) -> bool:
        sn = len(s)
        pn = len(p)

        if s == "":
            for ch in p:
                if ch != "*":
                    return False
            return True

        if pn > 0:
            pp = p[0]
            for i in range(1, pn):
                if p[i] == "*" and p[i - 1] == p[i]:
                    continue
                pp += p[i]

            p = pp
            pn = len(p)

        dp = [[False for i in range(sn + 1)] for i in range(pn + 1)]

        dp[0][0] = True

        if pn > 0 and p[0] == "*":
            dp[1][0] = True

        def printdp():
            for i in range(pn + 1):
                for j in range(sn + 1):
                    print(dp[i][j], " ", end="")
                print()

        for i in range(1, pn + 1):
            for j in range(1, sn + 1):
                sch = s[j - 1]
                pch = p[i - 1]

                if pch == "*" and (dp[i - 1][j] or dp[i][j - 1]):
                    dp[i][j] = True
                elif (pch == "?" or sch == pch) and dp[i - 1][j - 1]:
                    dp[i][j] = True

        # printdp()
        return dp[pn][sn]
#
# if __name__ == "__main__":
#     s = input()[1:-1]
#     p = input()[1:-1]
#     res = Solution().isMatch(s, p)
#     print(res)
