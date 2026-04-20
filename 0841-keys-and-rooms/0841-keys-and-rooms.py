class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        n = len(rooms)

        def dfs(node):
            for room in rooms[node]:
                if room not in visited:
                    visited.add(room)
                    dfs(room)
        
        visited = {0}
        dfs(0)

        return len(visited) == n