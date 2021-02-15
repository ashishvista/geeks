class Solution(object):
    def makeConnected(self, n, connections):
        if len(connections) < n-1:
            return -1

        # self.g = [[0 for i in range(n)] for i in range(n)]

        self.dsu = [-1 for i in range(n)]

        redundant_edges_count = 0
        for ed in connections:
            u = ed[0]
            v = ed[1]
            # self.g[u][v] = 1
            # self.g[v][u] = 1
            redundant_edges_count += self.union(u, v)

        disconnected_computers_count = self.getDisconnectedComponents(n)

        # self.printAdj()
        # print(self.dsu)
        # print(disconnected_computers_count)
        if redundant_edges_count >= disconnected_computers_count - 1:
            return disconnected_computers_count - 1
        else:
            return -1

    def find(self, u, icount=0):
        if self.dsu[u] == -1:
            return {"leader": u, "icount": icount}
        else:
            res = self.find(self.dsu[u], icount + 1)
            self.dsu[u] = res["leader"]
            return res

    def union(self, u, v):

        luh = self.find(u)
        lvh = self.find(v)

        lu = luh["leader"]
        lv = lvh["leader"]

        lui = luh["icount"]
        lvi = lvh["icount"]

        if lu != lv:
            if lui > lvi:
                self.dsu[lv] = lu
            elif lvi >= lui:
                self.dsu[lu] = lv
            return 0
        else:
            return 1

    def getDisconnectedComponents(self, n):
        dc = set()
        for i in range(n):
            dc.add(self.find(i)["leader"])
        return len(dc)

    def printAdj(self):
        for u in self.g:
            s = ""
            for v in u:
                s += str(v) + ","
            s = s[:-1]
            print(s)


if __name__ == "__main__":
    n = int(input())
    st = input().strip()[2:-2]
    st = list(st.split("],["))
    arr = []
    for ed in st:
        arr.append(list(map(int, ed.split(","))))
    ss = Solution().makeConnected(n, arr)
    print(ss)
