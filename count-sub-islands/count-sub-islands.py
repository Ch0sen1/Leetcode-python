class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])
        
        res = 0
                    
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid2[i][j] == 0:
                return
            
            grid2[i][j] = 0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i,j)
                    
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    dfs(i,j)
                    res += 1
        
        return res
                    
        
        
        