from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.g = defaultdict(list)
        self.visited = defaultdict(int)
        self.ne = 0
        self.ce = 0
        for ed in tickets:
            u = ed[0]
            v = ed[1]
            self.ne += 1
            self.g[u].append(v)
            key = str(u) + "-" + str(v)
            self.visited[key] += 1

        for k in self.g:
            varr = self.g[k]
            varr.sort()

        self.res = []
        self.dfs("JFK")
        return self.res

    def dfs(self, u):
        self.res.append(u)
        if self.ce == self.ne:
            return True
        for v in self.g[u]:
            key = str(u) + "-" + str(v)
            if self.visited[key] > 0:
                self.visited[key] -= 1
                self.ce += 1
                if self.dfs(v):
                    return True
                self.visited[key] += 1
                self.ce -= 1
        self.res.pop()
        return False
