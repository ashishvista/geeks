from collections import defaultdict, deque

from typing import List


class Node:
    current_buses = None
    total_bus_taken = None
    destination_reached_flag = None

    def __init__(self, u):
        self.current_buses = []
        self.total_bus_taken = 1
        self.u = u


class Solution:
    def numBusesToDestination1(self, routes: List[List[int]], S: int, T: int) -> int:
        self.g = defaultdict(list)
        self.busRoutes = {}
        self.visited = {}
        self.starting_buses = set()
        i = 0
        if S == T:
            return 0
        for route in routes:
            bus = i
            self.busRoutes[bus] = set(route)
            if S in self.busRoutes[bus] and T in self.busRoutes[bus]:
                return 1
            for j in range(1, len(route)):
                u = route[j - 1]
                v = route[j]
                if u == S:
                    self.starting_buses.add(bus)
                self.g[u].append(v)

            if len(route) > 1:
                u = v
                v = route[0]
                self.g[u].append(v)
                if u == S:
                    self.starting_buses.add(bus)

            i += 1

        # print(self.g)
        # print(self.starting_buses)
        # print(self.busRoutes)
        dq = deque()
        snode = Node(S)
        snode.current_buses = self.starting_buses
        dq.append(snode)
        return self.bfs(S, T, dq)

    def bfs1(self, S, T, dq):

        self.visited[S] = 1
        mnn = float("+inf")
        while dq:
            unode = dq.popleft()
            u = unode.u

            if u == T:
                mnn = min(mnn, unode.total_bus_taken)
                return mnn

            current_buses = unode.current_buses

            for b in current_buses:
                if T in self.busRoutes[b]:
                    mnn = min(mnn, unode.total_bus_taken)
                    return mnn

            for v in self.g[u]:
                if v not in self.visited:
                    self.visited[v] = 1
                    tmp_current_buses = []
                    vnode = Node(v)
                    for b in current_buses:
                        if v in self.busRoutes[b]:
                            tmp_current_buses.append(b)

                    if len(tmp_current_buses) == 0:
                        vnode.total_bus_taken = unode.total_bus_taken + 1
                        for b in range(len(self.busRoutes)):
                            if u in self.busRoutes[b] and v in self.busRoutes[b]:
                                tmp_current_buses.append(b)
                    else:
                        vnode.total_bus_taken = unode.total_bus_taken

                    vnode.current_buses = tmp_current_buses
                    if mnn == 2:
                        return mnn
                    dq.append(vnode)

        if mnn == float("+inf"):
            return -1
        else:
            return mnn

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        self.g = defaultdict(list)
        self.N = len(routes)

        routes = list(map(set, routes))
        starting_buses = set()
        end_buses = set()

        for i, route in enumerate(routes):
            if S in route:
                starting_buses.add(i)
            if T in route:
                end_buses.add(i)
            for j in range(i + 1, len(routes)):
                proute = routes[j]
                if self.isIntersect(route, proute):
                    self.g[i].append(j)
                    self.g[j].append(i)

        dq = deque()
        visited = set()
        dist = [float("+inf") for i in range(self.N)]
        for sb in starting_buses:
            if sb in end_buses:
                return 1
            dq.append(sb)
            visited.add(sb)
            dist[sb] = 1

        return self.bfs(dq, visited, dist, end_buses)

    def bfs(self, dq, visited, dist, end_buses):
        while dq:
            u = dq.popleft()
            if u in end_buses:
                return dist[u]

            for v in self.g[u]:
                if v not in visited:
                    visited.add(v)
                    dq.append(v)
                    dist[v] = dist[u] + 1
        return -1

    def isIntersect(self, l1, l2):

        for ele in l2:
            if ele in l1:
                return True

        return False


if __name__ == "__main__":
    n = int(input())
    routes = []
    for i in range(n):
        temp = list(map(int, input().strip()[1:-2].split(",")))
        routes.append(temp)
    S = int(input())
    T = int(input())
    res = Solution().numBusesToDestination(routes, S, T)
    print(res)
