class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = len(grid)
        cols = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(cols):
                if grid[i][j] < 0:
                    res += 1
        return res
                
        
        