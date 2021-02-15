from typing import List


def makeAdjMatrix(n, p):
    matrix = [[] for i in range(n)]
    for i in p:
        matrix[i[0]].append(i[1])
    return matrix


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        matrix = makeAdjMatrix(numCourses, prerequisites)
        res = self.findCyclic(numCourses, matrix)
        # print("any cycle", res)
        if res:
            return False
        else:
            return True

    def findCyclic(self, n, matrix):
        visited = [False for i in range(n)]
        ss = [False for i in range(n)]

        for u in range(n):
            if not visited[u]:
                flag = self.finCyclicUtil(visited, ss, matrix, u)
                if flag:
                    return True

        return False

    def finCyclicUtil(self, visited, ss, matrix, u):

        if ss[u]:
            return True

        if visited[u]:
            return False
        else:
            visited[u] = True
            ss[u] = True

        for v in matrix[u]:

            flag = self.finCyclicUtil(visited, ss, matrix, v)
            if flag:
                return True
        ss[u] = False
        return False
