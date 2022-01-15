class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        
        
        def dfs(room):
            for neigh in rooms[room]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)
        
        dfs(0)
                
        return len(visited) == len(rooms)
        