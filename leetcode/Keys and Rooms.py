class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        print()
        V = len(rooms)
        visited = {0: True}
        for v in rooms[0]:
            self.dfs(rooms, visited, v)
        if len(visited) == V:
            return True
        else:
            return False

    def dfs(self, rooms, visited, u):
        if u in visited:
            return True
        visited[u] = True
        for v in rooms[u]:
            self.dfs(rooms, visited, v)
