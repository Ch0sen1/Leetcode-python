class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        color = 2
        color_size = Counter()
        
        
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        
        def paint(i, j, color):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
                grid[i][j] = color
                color_size[color] += 1
                for dx, dy in dirs:
                    paint(i+dx, j+dy, color)
                
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 1:
                    continue
                paint(i, j, color)
                color += 1
                
        ans = max(color_size.values() or [0])
        
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    continue
                near_color = set()
                for dx, dy in dirs:
                    newx, newy = i + dx, j + dy
                    if newx < 0 or newx >= rows or newy < 0 or newy >= cols or grid[newx][newy] == 0:
                        continue
                    near_color.add(grid[newx][newy])
                affect_area = 1
                for color in near_color:
                    affect_area += color_size[color]
                
                ans = max(ans, affect_area)
        
        return ans
                    
        
                
        
                
                
        