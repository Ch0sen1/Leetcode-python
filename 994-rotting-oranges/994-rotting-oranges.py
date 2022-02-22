class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(1,0), (-1,0),(0,-1),(0,1)]
        
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        step = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for dx, dy in dirs:
                    newx, newy = r + dx, c + dy
                    if 0 <= newx < rows and 0 <= newy < cols and grid[newx][newy] == 1:
                        grid[newx][newy] = 2
                        q.append((newx, newy))
            
            step += 1
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return max(0, step-1)
            