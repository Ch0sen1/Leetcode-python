class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldcolor = image[sr][sc]
        
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        
        if oldcolor != newColor:
            q = deque()

            q.append((sr,sc))

            while q:
                x, y = q.popleft()
                if x < 0 or x >= len(image) or y < 0 or y >= len(image[0])  or image[x][y] != oldcolor:
                    continue
                image[x][y] = newColor
                for dx, dy in dirs:
                    newx, newy = x+dx, y+dy
                    q.append((newx, newy))
        
        return image
        
        