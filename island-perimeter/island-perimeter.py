class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.res = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    self.sum_adj(grid, i, j)
        
        return self.res
        
        
    def sum_adj(self, grid, i, j):
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for dx, dy in dirs:
            x = i + dx
            y = j + dy
            if x < 0  or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
                self.res +=1
        
        
        
        