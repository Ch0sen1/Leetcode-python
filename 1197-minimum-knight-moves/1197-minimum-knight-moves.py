class Solution:
    def minKnightMoves(self, fx: int, fy: int) -> int:
        q = deque()
        visited = set()
        visited.add((0,0))
        
        fx = abs(fx)
        fy = abs(fy)
        dirs = [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1)]
        
        q.append((0,0,0))
        
        while q:
            x, y, step = q.popleft()
            if (x,y) == (fx,fy):
                return step
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and -1 <= nx <= fx+2 and -1 <= ny <= fy+2:
                    visited.add((nx,ny))
                    q.append((nx, ny, step+1))
        return -1
                
                
          
        