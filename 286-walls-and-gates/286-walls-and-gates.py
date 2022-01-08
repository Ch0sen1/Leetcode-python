class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols = len(rooms[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        q = deque()
        visited = set()
        
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    q.append((i,j, 0))
                    
        while q:
            x, y, step = q.popleft()
            if (0 <= x < rows and 0 <= y < cols and (x,y) not in visited and rooms[x][y] not in [0 , -1]) or step == 0:
                rooms[x][y] = step
                visited.add((x,y))
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    q.append((nx, ny, step+1))
                    