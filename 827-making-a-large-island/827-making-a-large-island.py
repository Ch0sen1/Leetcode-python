class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        color = 2
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        
        color_size = Counter()
        
        # first iteration, collect the size of differnt color, while makring them to differnt color
        def paint(i, j, color):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
                grid[i][j] = color
                color_size[color] += 1
                for dx, dy in dirs:
                    paint(i+dx, j+dy, color)
        
        # 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 1:
                    continue
                paint(i, j, color)
                color += 1
        
        # ans = max(0, max(color_size.values()))
        
        ans = max(color_size.values() or [0] )
        
        # find the 0 that connect those island
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    continue
                near_color = set()
                for dx,dy in dirs:
                    new_x, new_y = i + dx, j + dy
                    if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols or grid[new_x][new_y] == 0:
                        continue
                    near_color.add(grid[new_x][new_y])
                
                affected_area = 1
                
                for color in near_color:
                    affected_area += color_size[color]
                
                ans = max(ans, affected_area)
                
        return ans 
                
                    
                    
        
        
                    
        
                
        
                
                
        