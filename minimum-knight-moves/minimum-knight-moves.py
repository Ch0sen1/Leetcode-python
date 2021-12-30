class Solution:
    def minKnightMoves(self, fx: int, fy: int) -> int:
        visited = set()
        visited.add((0,0))
        q = deque()
        q.append([0,0,0])
        ## put it to positive, so only move one direaction
        fx = abs(fx)
        fy = abs(fy)
        
        while q:
            x, y, step = q.popleft()
            if (x,y) == (fx,fy):
                return step
            for dx, dy in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1),(-1,-2),(-2,-1)]:
                if (x+dx, y+dy) not in visited and -1 <= x+dx <= fx+2 and -1 <= y+dy <= fy+2:
                    visited.add((x+dx, y+dy))
                    q.append((x+dx,y+dy,step+1))
                
        return -1   
        