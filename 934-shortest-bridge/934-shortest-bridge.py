class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def getFirstIsland():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return i,j
        
        
        
        startx, starty = getFirstIsland()
        q = deque()
        step = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def dfs(x, y):
            q.append((x,y))
            grid[x][y] = 0
            for dx,dy in dirs:
                newx, newy = x+dx, y+dy
                if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == 1:
                    dfs(newx, newy)
        
        dfs(startx, starty)
        
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in dirs:
                    newx, newy = x+dx, y+dy
                    if 0 <= newx < m and 0 <= newy < n:
                        if grid[newx][newy] == 1:
                            return step
                        elif grid[newx][newy] == 0:
                            grid[newx][newy] = 3
                            q.append((newx, newy))
            step += 1
        
        return step
                
            
            
        