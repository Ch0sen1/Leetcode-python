class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        self.dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    res = max(area, res)
                    
        return res
    
    def dfs(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
            return 0
        
        maxArea = 1
        grid[x][y] = 0
        for dx, dy in self.dirs:
            newx, newy = x+dx, y+dy
            maxArea += self.dfs(grid, newx, newy)
        return maxArea
            
        
        
        