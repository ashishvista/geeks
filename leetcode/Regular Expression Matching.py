class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sn = len(s)
        pn = len(p)

        if s == "":
            while True:
                i = 0
                if i + 1 < len(p) and p[i + 1] == "*":
                    p = p[i + 2:]
                else:
                    break

            if len(p) > 0:
                return False
            else:
                return True

        dp = [[False for i in range(sn + 1)] for i in range(pn + 1)]

        dp[0][0] = True

        def printdp():
            for i in range(pn + 1):
                for j in range(sn + 1):
                    if dp[i][j]:
                        print(dp[i][j], "  ", end="")
                    else:
                        print(dp[i][j], " ", end="")

                print()

        # for i in range(1, sn + 1):
        #     dp[0][i] = False
        #
        # for i in range(1, pn + 1):
        #     dp[i][0] = False

        for i in range(1, pn + 1):
            flag = False
            for j in range(1, sn + 1):
                sch = s[j - 1]
                pch = p[i - 1]

                if pch == "*" and p[i - 2] == ".":
                    fflag = False
                    for k in range(1, sn + 1):
                        if dp[i - 1][k]:
                            fflag = True
                            break

                    for kk in range(0, sn + 1):
                        dp[i][kk] = dp[i - 2][kk]

                    if not fflag:
                        break

                    dp[i][k - 1] = True

                    if k == 1:
                        dp[i][0] = True
                    for m in range(k, sn + 1):
                        dp[i][m] = True

                    flag = True
                    break
                elif pch == "*":
                    c = 1
                    arr = []

                    for k in range(c, sn + 1):
                        if dp[i - 1][k]:
                            arr.append(k)
                    tch = p[i - 2]
                    for k in range(0, sn + 1):
                        dp[i][k] = dp[i - 2][k]

                    for k in arr:
                        for m in range(k, sn + 1):
                            if s[m - 1] != tch:
                                break
                            else:
                                dp[i][m] = True
                    if len(arr) == 0 and i == 2:
                        dp[i][0] = True

                    flag = True
                    break
                elif (pch == "." or sch == pch) and dp[i - 1][j - 1]:
                    flag = True
                    dp[i][j] = True
                    continue
                # else:
                #     dp[i][j] = False

            # if not flag and i < pn and p[i] != "*":
            #     printdp()
            #     return False

        printdp()
        return dp[pn][sn]
    def isMatch(self, s: str, p: str) -> bool:
        sn = len(s)
        pn = len(p)

        if s == "":
            while True:
                i = 0
                if i + 1 < len(p) and p[i + 1] == "*":
                    p = p[i + 2:]
                else:
                    break

            if len(p) > 0:
                return False
            else:
                return True

        dp = [[False for i in range(sn + 1)] for i in range(pn + 1)]

        dp[0][0] = True

        def printdp():
            for i in range(pn + 1):
                for j in range(sn + 1):
                    if dp[i][j]:
                        print(dp[i][j], "  ", end="")
                    else:
                        print(dp[i][j], " ", end="")

                print()

        for i in range(1, pn + 1):
            flag = False
            for j in range(1, sn + 1):
                sch = s[j - 1]
                pch = p[i - 1]

                if pch == "*" and p[i - 2] == ".":
                    break
                elif pch == "*":
                    flag = True
                    break
                elif (pch == "." or sch == pch) and dp[i - 1][j - 1]:
                    flag = True
                    dp[i][j] = True
                    continue

        printdp()
        return dp[pn][sn]


if __name__ == "__main__":
    s = input()[1:-1]
    p = input()[1:-1]
    res = Solution().isMatch(s, p)
    print(res)
