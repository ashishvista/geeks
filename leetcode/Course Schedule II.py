from collections import defaultdict, deque


class Solution:
    def findOrder1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.g = defaultdict(list)
        self.visited = set()
        self.topo = []
        self.set = set()

        for u in range(numCourses):
            self.g[u] = []

        for p in prerequisites:
            u = p[1]
            v = p[0]
            self.g[u].append(v)

        for u in self.g:
            if u not in self.visited:
                if not self.dfs(u):
                    return []

        self.topo.reverse()
        return self.topo

    def dfs(self, u):

        self.visited.add(u)
        self.set.add(u)
        for v in self.g[u]:
            if v not in self.visited:
                if not self.dfs(v):
                    return False
            elif v in self.set:
                return False

        self.set.remove(u)
        self.topo.append(u)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        dq = deque()
        topo = []
        indegree = [0 for i in range(numCourses)]

        for u in range(numCourses):
            g[u] = []

        for p in prerequisites:
            u = p[1]
            v = p[0]
            g[u].append(v)
            indegree[v] += 1

        for u in range(numCourses):
            if indegree[u] == 0:
                dq.append(u)

        while dq:
            u = dq.popleft()
            topo.append(u)
            for v in g[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    dq.append(v)

        for u in range(numCourses):
            if indegree[u] > 0:
                return []
        return topo
