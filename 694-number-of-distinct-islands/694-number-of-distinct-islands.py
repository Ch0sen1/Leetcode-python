from typing import List
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        unique = set()
        
        path = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(i, j, path, "o", grid)
                    unique.add(''.join(path))
                    path = []
                
        return len(unique)
        
        
    def dfs(self, i, j, path, dirs, grid):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                path.append(dirs)
                self.dfs(i+1, j, path, 'd', grid)
                self.dfs(i-1, j, path, 'u', grid)
                self.dfs(i, j-1, path, 'l', grid)
                self.dfs(i, j+1, path, 'r', grid)
                path.append('b')
                

                
                
        