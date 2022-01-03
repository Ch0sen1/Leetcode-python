class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols = len(rooms[0])
        visited = set()
        
        
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c,0))
                
        while q:
            row , col, step = q.popleft()
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or (rooms[row][col] in [0, -1] and step!= 0):
                continue
            rooms[row][col] = step
            visited.add((row,col))
            dirs = [(0,1),(0,-1),(-1,0),(1,0)]
            for dx, dy in dirs:
                q.append((row+dx, col+dy, step+1))
                