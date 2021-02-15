from collections import deque, defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
        dq = deque()
        g = defaultdict(set)

        for ed in edges:
            g[ed[0]].add(ed[1])
            g[ed[1]].add(ed[0])

        for u in g:
            if len(g[u]) == 1:
                dq.append(u)

        while len(g) > 2:
            ln = len(dq)
            while ln > 0:
                u = dq.popleft()
                for v in g[u]:
                    g[v].remove(u)
                    if len(g[v]) == 1:
                        dq.append(v)
                del g[u]
                ln -= 1
        return list(dq)
